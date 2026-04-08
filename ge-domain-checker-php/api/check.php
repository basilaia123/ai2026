<?php
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');

const DEFAULT_LOOKUP_ENDPOINTS = [
    'https://rdap.org/domain/{domain}',
    'https://www.rdap.net/domain/{domain}',
];
const DEFAULT_NIC_WEB_WHOIS_ENDPOINT = 'https://nic.ge/en/find?domain={domain}';
const DEFAULT_LOOKUP_TIMEOUT_MS = 12000;
const DEFAULT_LOOKUP_MIN_INTERVAL_MS = 1100;
const DEFAULT_LOOKUP_MAX_RETRIES = 2;
const DEFAULT_WHOIS_HOST = 'whois.nic.ge';
const DEFAULT_WHOIS_PORT = 43;
const DEFAULT_WHOIS_TIMEOUT_MS = 9000;

function json_response(int $status, array $payload): void
{
    http_response_code($status);
    echo json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    exit;
}

function ends_with(string $value, string $suffix): bool
{
    if ($suffix === '') {
        return true;
    }
    $len = strlen($suffix);
    if ($len > strlen($value)) {
        return false;
    }
    return substr($value, -$len) === $suffix;
}

function sanitize_input(string $value): string
{
    $clean = trim($value);
    $clean = preg_replace('#^https?://#i', '', $clean) ?? '';
    $clean = preg_replace('/[\/?#].*$/', '', $clean) ?? '';
    $clean = rtrim($clean, '.');
    if (function_exists('mb_strtolower')) {
        $clean = mb_strtolower($clean, 'UTF-8');
    } else {
        $clean = strtolower($clean);
    }
    return $clean;
}

function normalize_domain(string $input): array
{
    $cleaned = sanitize_input($input);
    if ($cleaned === '') {
        return ['ok' => false, 'reason' => 'ცარიელი ჩანაწერია.'];
    }

    $domain = ends_with($cleaned, '.ge') ? $cleaned : ($cleaned . '.ge');

    if (function_exists('idn_to_ascii')) {
        $variant = defined('INTL_IDNA_VARIANT_UTS46') ? INTL_IDNA_VARIANT_UTS46 : 0;
        $asciiDomain = @idn_to_ascii($domain, 0, $variant);
    } else {
        $asciiDomain = $domain;
    }

    if (!$asciiDomain) {
        return ['ok' => false, 'reason' => 'დომენის ფორმატი არასწორია.'];
    }

    $asciiDomain = strtolower($asciiDomain);
    if (!ends_with($asciiDomain, '.ge')) {
        return ['ok' => false, 'reason' => 'მხოლოდ .ge დომენებია მხარდაჭერილი.'];
    }

    $label = substr($asciiDomain, 0, -3);
    $labelValid = preg_match('/^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$/i', $label) === 1;
    if (!$labelValid) {
        return [
            'ok' => false,
            'reason' => 'დომენი უნდა იყოს 1-63 სიმბოლო, მხოლოდ ასო/ციფრი/დეფისი.',
        ];
    }

    return [
        'ok' => true,
        'label' => $label,
        'ascii_domain' => $label . '.ge',
        'display_domain' => ends_with($cleaned, '.ge') ? $cleaned : ($cleaned . '.ge'),
    ];
}

function get_premium_tier(int $score): string
{
    if ($score >= 85) return 'premium';
    if ($score >= 70) return 'strong';
    if ($score >= 55) return 'good';
    if ($score >= 40) return 'average';
    return 'weak';
}

function calculate_premium_score(string $label): array
{
    $normalized = strtolower($label);
    $length = strlen($normalized);
    $lettersOnly = preg_replace('/[^a-z]/', '', $normalized) ?? '';
    $withoutHyphen = str_replace('-', '', $normalized);
    $withoutHyphenLength = strlen($withoutHyphen);
    $uniqueCount = count(array_unique(str_split($withoutHyphen)));
    $hyphenCount = substr_count($normalized, '-');
    preg_match_all('/[0-9]/', $normalized, $digits);
    $digitCount = count($digits[0]);
    preg_match_all('/[aeiouy]/', $lettersOnly, $vowels);
    $vowelCount = count($vowels[0]);
    $consonantCount = max(0, strlen($lettersOnly) - $vowelCount);
    $vowelRatio = strlen($lettersOnly) > 0 ? ($vowelCount / strlen($lettersOnly)) : 0;
    $uniqueRatio = $withoutHyphenLength > 0 ? ($uniqueCount / $withoutHyphenLength) : 0;

    $score = 50;

    if ($length <= 4) $score += 30;
    elseif ($length <= 6) $score += 24;
    elseif ($length <= 8) $score += 16;
    elseif ($length <= 12) $score += 8;
    elseif ($length <= 18) $score += 2;
    else $score -= 8;

    if ($hyphenCount === 0) $score += 10;
    else $score -= min(18, $hyphenCount * 8);

    if ($digitCount === 0) $score += 8;
    elseif ($digitCount === 1) $score += 2;
    else $score -= min(12, $digitCount * 3);

    if ($vowelRatio >= 0.35 && $vowelRatio <= 0.6) $score += 8;
    elseif ($vowelRatio > 0 && $vowelRatio < 0.2) $score -= 6;

    if ($consonantCount >= 2 && $vowelCount >= 1) $score += 3;
    if ($uniqueRatio >= 0.7) $score += 6;
    elseif ($uniqueRatio <= 0.4) $score -= 6;

    if (preg_match('/(.)\1\1/', $normalized) === 1) $score -= 10;
    if (strlen($lettersOnly) >= 10 && $vowelCount <= 1) $score -= 12;

    $safeScore = max(0, min(100, (int) round($score)));
    return [
        'score' => $safeScore,
        'tier' => get_premium_tier($safeScore),
    ];
}

function text_contains_any(string $haystack, array $needles): bool
{
    foreach ($needles as $needle) {
        if ($needle !== '' && strpos($haystack, $needle) !== false) {
            return true;
        }
    }
    return false;
}

function parse_http_status_from_headers(array $headers): int
{
    foreach ($headers as $headerLine) {
        if (preg_match('#^HTTP/\S+\s+(\d{3})#i', (string) $headerLine, $matches) === 1) {
            return (int) $matches[1];
        }
    }
    return 0;
}

function get_lookup_endpoints(): array
{
    $raw = getenv('LOOKUP_ENDPOINTS');
    if (is_string($raw) && trim($raw) !== '') {
        $items = array_values(array_filter(array_map('trim', explode(',', $raw))));
        if (count($items) > 0) {
            return $items;
        }
    }

    $single = getenv('LOOKUP_ENDPOINT');
    if (is_string($single) && trim($single) !== '') {
        return [trim($single)];
    }

    return DEFAULT_LOOKUP_ENDPOINTS;
}

function apply_lookup_rate_limit(): void
{
    static $lastLookupAtMs = 0.0;

    $intervalMs = (int) (getenv('LOOKUP_MIN_INTERVAL_MS') ?: DEFAULT_LOOKUP_MIN_INTERVAL_MS);
    $intervalMs = max(0, $intervalMs);
    if ($intervalMs === 0) {
        return;
    }

    $nowMs = microtime(true) * 1000;
    $elapsed = $nowMs - $lastLookupAtMs;
    if ($lastLookupAtMs > 0 && $elapsed < $intervalMs) {
        $sleepMs = (int) ceil($intervalMs - $elapsed);
        if ($sleepMs > 0) {
            usleep($sleepMs * 1000);
        }
    }

    $lastLookupAtMs = microtime(true) * 1000;
}

function http_get(string $url, int $timeoutMs): array
{
    if (function_exists('curl_init')) {
        $ch = curl_init($url);
        if (!$ch) {
            return ['ok' => false, 'status' => 0, 'body' => '', 'error' => 'curl_init failed'];
        }

        curl_setopt_array($ch, [
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_CONNECTTIMEOUT_MS => min(5000, $timeoutMs),
            CURLOPT_TIMEOUT_MS => $timeoutMs,
            CURLOPT_HTTPHEADER => [
                'Accept: application/json, text/plain;q=0.8, */*;q=0.5',
                'User-Agent: GEDomainCheckerPHP/1.1',
            ],
        ]);

        $body = curl_exec($ch);
        $status = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
        $error = curl_error($ch);
        curl_close($ch);

        if ($body === false) {
            return ['ok' => false, 'status' => $status, 'body' => '', 'error' => $error ?: 'cURL error'];
        }

        return ['ok' => true, 'status' => $status, 'body' => (string) $body, 'error' => ''];
    }

    $timeoutSeconds = max(2, (int) ceil($timeoutMs / 1000));
    $context = stream_context_create([
        'http' => [
            'method' => 'GET',
            'timeout' => $timeoutSeconds,
            'ignore_errors' => true,
            'header' => "Accept: application/json, text/plain;q=0.8, */*;q=0.5\r\nUser-Agent: GEDomainCheckerPHP/1.1\r\n",
        ],
    ]);

    $body = @file_get_contents($url, false, $context);
    $headers = $http_response_header ?? [];
    $status = parse_http_status_from_headers($headers);

    if ($body === false) {
        $err = error_get_last();
        return ['ok' => false, 'status' => $status, 'body' => '', 'error' => $err['message'] ?? 'HTTP request failed'];
    }

    return ['ok' => true, 'status' => $status, 'body' => (string) $body, 'error' => ''];
}

function nic_web_whois_lookup(string $domain): array
{
    $endpointTemplate = getenv('NIC_WEB_WHOIS_ENDPOINT') ?: DEFAULT_NIC_WEB_WHOIS_ENDPOINT;
    $timeoutMs = (int) (getenv('LOOKUP_TIMEOUT_MS') ?: DEFAULT_LOOKUP_TIMEOUT_MS);

    if (strpos($endpointTemplate, '{domain}') !== false) {
        $url = str_replace('{domain}', rawurlencode($domain), $endpointTemplate);
    } else {
        $separator = strpos($endpointTemplate, '?') === false ? '?' : '&';
        $url = rtrim($endpointTemplate, '&?') . $separator . 'domain=' . rawurlencode($domain);
    }

    apply_lookup_rate_limit();
    $response = http_get($url, max(3000, $timeoutMs));
    if (!$response['ok']) {
        throw new RuntimeException('NIC web whois request failed: ' . ($response['error'] ?: 'network error'));
    }

    $httpStatus = (int) $response['status'];
    $body = (string) $response['body'];
    $upper = strtoupper($body);
    $domainUpper = strtoupper($domain);

    if ($httpStatus < 200 || $httpStatus >= 300) {
        return [
            'status' => 'unknown',
            'available' => null,
            'note' => "NIC web whois HTTP {$httpStatus}.",
        ];
    }

    if (text_contains_any($upper, ['WHOIS IS TEMPORARILY UNAVAILABLE', 'SERVICE IS TEMPORARILY UNAVAILABLE'])) {
        return [
            'status' => 'unknown',
            'available' => null,
            'note' => 'NIC WHOIS is temporarily unavailable.',
        ];
    }

    if (text_contains_any($upper, ['DOMAIN-STATUS--BUSY', 'DOMAIN IS UNAVAILABLE'])) {
        return ['status' => 'taken', 'available' => false];
    }

    if (text_contains_any($upper, ['DOMAIN-STATUS--FREE', 'DOMAIN IS AVAILABLE'])) {
        return ['status' => 'available', 'available' => true];
    }

    if (
        text_contains_any($upper, ['NO MATCH FOR', 'NO ENTRIES FOUND']) &&
        strpos($upper, $domainUpper) !== false
    ) {
        return ['status' => 'available', 'available' => true];
    }

    if (
        text_contains_any($upper, ['DOMAIN NAME:', 'REGISTRY EXPIRY DATE:', 'REGISTRAR:']) &&
        strpos($upper, $domainUpper) !== false
    ) {
        return ['status' => 'taken', 'available' => false];
    }

    return [
        'status' => 'unknown',
        'available' => null,
        'note' => 'NIC web whois პასუხი ვერ განისაზღვრა.',
    ];
}

function parse_lookup_response(int $httpStatus, string $body, string $domain): array
{
    $upper = strtoupper($body);
    $json = json_decode($body, true);
    $domainUpper = strtoupper($domain);

    if ($httpStatus === 404 || $httpStatus === 410) {
        return [
            'status' => 'unknown',
            'available' => null,
            'note' => "HTTPS lookup HTTP {$httpStatus} (not authoritative for availability).",
        ];
    }

    if ($httpStatus >= 200 && $httpStatus < 300) {
        if (is_array($json)) {
            $errorCode = isset($json['errorCode']) ? (int) $json['errorCode'] : 0;
            if ($errorCode === 404) {
                return [
                    'status' => 'unknown',
                    'available' => null,
                    'note' => 'RDAP errorCode=404 (not authoritative for availability).',
                ];
            }

            $title = strtoupper((string) ($json['title'] ?? ''));
            $description = '';
            if (isset($json['description'])) {
                if (is_array($json['description'])) {
                    $description = strtoupper(implode(' ', array_map('strval', $json['description'])));
                } else {
                    $description = strtoupper((string) $json['description']);
                }
            }

            if (
                text_contains_any($title . ' ' . $description, ['NOT FOUND', 'NO MATCH']) &&
                strpos($title . ' ' . $description, $domainUpper) !== false
            ) {
                return ['status' => 'available', 'available' => true];
            }

            if (
                !empty($json['ldhName']) ||
                (!empty($json['objectClassName']) && strtolower((string) $json['objectClassName']) === 'domain') ||
                !empty($json['unicodeName']) ||
                isset($json['events'])
            ) {
                return ['status' => 'taken', 'available' => false];
            }
        }

        if (
            text_contains_any($upper, ['NO MATCH FOR', 'NO ENTRIES FOUND']) &&
            strpos($upper, $domainUpper) !== false
        ) {
            return ['status' => 'available', 'available' => true];
        }

        if (text_contains_any($upper, ['DOMAIN NAME:', 'REGISTRY EXPIRY DATE:', 'REGISTRAR:', '"LDHNAME"', '"OBJECTCLASSNAME":"DOMAIN"'])) {
            return ['status' => 'taken', 'available' => false];
        }

        return [
            'status' => 'unknown',
            'available' => null,
            'note' => 'HTTPS პასუხი ვერ განისაზღვრა.',
        ];
    }

    if ($httpStatus === 429) {
        return [
            'status' => 'unknown',
            'available' => null,
            'note' => 'HTTPS lookup rate limited (HTTP 429).',
        ];
    }

    return [
        'status' => 'unknown',
        'available' => null,
        'note' => "HTTPS lookup HTTP {$httpStatus}.",
    ];
}

function https_lookup(string $domain): array
{
    $endpoints = get_lookup_endpoints();
    $timeoutMs = (int) (getenv('LOOKUP_TIMEOUT_MS') ?: DEFAULT_LOOKUP_TIMEOUT_MS);
    $maxRetries = (int) (getenv('LOOKUP_MAX_RETRIES') ?: DEFAULT_LOOKUP_MAX_RETRIES);
    $maxRetries = max(0, $maxRetries);
    $notes = [];

    foreach ($endpoints as $endpointTemplate) {
        for ($attempt = 0; $attempt <= $maxRetries; $attempt += 1) {
            if (strpos($endpointTemplate, '{domain}') !== false) {
                $url = str_replace('{domain}', rawurlencode($domain), $endpointTemplate);
            } else {
                $url = rtrim($endpointTemplate, '/') . '/' . rawurlencode($domain);
            }

            apply_lookup_rate_limit();
            $response = http_get($url, max(3000, $timeoutMs));
            if (!$response['ok']) {
                $notes[] = "request error on {$endpointTemplate}: " . ($response['error'] ?: 'network error');
                break;
            }

            $parsed = parse_lookup_response((int) $response['status'], (string) $response['body'], $domain);
            if ((int) $response['status'] === 429) {
                $notes[] = "rate-limited by {$endpointTemplate}";
                if ($attempt < $maxRetries) {
                    usleep((int) (1200 * 1000 * ($attempt + 1)));
                    continue;
                }
                break;
            }

            return $parsed;
        }
    }

    $noteText = count($notes) ? implode('; ', $notes) : 'lookup endpoints unavailable';
    throw new RuntimeException($noteText);
}

function dns_indicates_taken(string $domain): ?bool
{
    if (!function_exists('dns_get_record')) {
        return null;
    }

    $nsRecords = @dns_get_record($domain, DNS_NS);
    if (is_array($nsRecords) && count($nsRecords) > 0) {
        return true;
    }

    $soaRecords = @dns_get_record($domain, DNS_SOA);
    if (is_array($soaRecords) && count($soaRecords) > 0) {
        return true;
    }

    $aRecords = @dns_get_record($domain, DNS_A);
    if (is_array($aRecords) && count($aRecords) > 0) {
        return true;
    }

    $aaaaRecords = @dns_get_record($domain, DNS_AAAA);
    if (is_array($aaaaRecords) && count($aaaaRecords) > 0) {
        return true;
    }

    return false;
}

function should_infer_available_from_lookup(array $parsed, ?bool $dnsTaken): bool
{
    if (($parsed['status'] ?? '') !== 'unknown') {
        return false;
    }

    if ($dnsTaken === true) {
        return false;
    }

    $noteUpper = strtoupper((string) ($parsed['note'] ?? ''));
    if (text_contains_any($noteUpper, ['HTTP 404', 'ERRORCODE=404', 'NOT AUTHORITATIVE FOR AVAILABILITY'])) {
        return true;
    }

    return false;
}

function parse_whois_result(string $rawText): array
{
    $upper = strtoupper($rawText);
    if (
        strpos($upper, 'NO MATCH FOR') !== false ||
        strpos($upper, 'NO ENTRIES FOUND') !== false ||
        strpos($upper, 'NOT FOUND') !== false
    ) {
        return ['status' => 'available', 'available' => true];
    }

    if (
        strpos($upper, 'DOMAIN NAME:') !== false ||
        strpos($upper, 'REGISTRY EXPIRY DATE:') !== false ||
        strpos($upper, 'REGISTRAR:') !== false
    ) {
        return ['status' => 'taken', 'available' => false];
    }

    return [
        'status' => 'unknown',
        'available' => null,
        'note' => 'WHOIS პასუხი ვერ განისაზღვრა.',
    ];
}

function whois_lookup(string $domain): string
{
    $host = getenv('WHOIS_HOST') ?: DEFAULT_WHOIS_HOST;
    $port = (int) (getenv('WHOIS_PORT') ?: DEFAULT_WHOIS_PORT);
    $timeoutMs = (int) (getenv('WHOIS_TIMEOUT_MS') ?: DEFAULT_WHOIS_TIMEOUT_MS);
    $timeoutSeconds = max(2, (int) ceil($timeoutMs / 1000));

    $errno = 0;
    $errstr = '';
    $fp = @fsockopen($host, $port, $errno, $errstr, $timeoutSeconds);
    if (!$fp) {
        throw new RuntimeException('WHOIS კავშირი ვერ დამყარდა: ' . $errstr);
    }

    stream_set_timeout($fp, $timeoutSeconds);
    fwrite($fp, $domain . "\r\n");

    $response = '';
    while (!feof($fp)) {
        $chunk = fgets($fp, 4096);
        if ($chunk === false) {
            break;
        }
        $response .= $chunk;
        if (strlen($response) > 100000) {
            break;
        }
    }

    $meta = stream_get_meta_data($fp);
    fclose($fp);

    if (!empty($meta['timed_out'])) {
        throw new RuntimeException('WHOIS timeout');
    }

    return $response;
}

function check_single_domain($input): array
{
    $inputString = (string) $input;
    $normalized = normalize_domain($inputString);
    if (empty($normalized['ok'])) {
        return [
            'input' => $inputString,
            'domain' => null,
            'status' => 'invalid',
            'available' => null,
            'premiumScore' => null,
            'premiumTier' => null,
            'note' => $normalized['reason'],
        ];
    }

    $premium = calculate_premium_score($normalized['label']);
    $socketFallbackEnabled = getenv('ENABLE_SOCKET_FALLBACK') === '1';

    $dnsTaken = dns_indicates_taken($normalized['ascii_domain']);
    if ($dnsTaken === true) {
        return [
            'input' => $inputString,
            'domain' => $normalized['display_domain'],
            'status' => 'taken',
            'available' => false,
            'premiumScore' => $premium['score'],
            'premiumTier' => $premium['tier'],
            'note' => 'DNS verification indicates domain is delegated (treated as taken).',
        ];
    }

    try {
        $parsed = nic_web_whois_lookup($normalized['ascii_domain']);

        if ($parsed['status'] === 'unknown') {
            $parsed = https_lookup($normalized['ascii_domain']);
        }

        if (should_infer_available_from_lookup($parsed, $dnsTaken)) {
            $parsed = [
                'status' => 'available',
                'available' => true,
                'note' => 'Inferred available: HTTPS 404 + no DNS delegation records found.',
            ];
        }

        if ($parsed['status'] === 'unknown' && $socketFallbackEnabled) {
            $raw = whois_lookup($normalized['ascii_domain']);
            $socketParsed = parse_whois_result($raw);
            if ($socketParsed['status'] !== 'unknown') {
                $parsed = $socketParsed;
            }
        }

        return [
            'input' => $inputString,
            'domain' => $normalized['display_domain'],
            'status' => $parsed['status'],
            'available' => $parsed['available'],
            'premiumScore' => $premium['score'],
            'premiumTier' => $premium['tier'],
            'note' => $parsed['note'] ?? null,
        ];
    } catch (Throwable $error) {
        if ($dnsTaken === true) {
            return [
                'input' => $inputString,
                'domain' => $normalized['display_domain'],
                'status' => 'taken',
                'available' => false,
                'premiumScore' => $premium['score'],
                'premiumTier' => $premium['tier'],
                'note' => 'HTTPS lookup failed, but DNS verification indicates domain is taken.',
            ];
        }

        if ($socketFallbackEnabled) {
            try {
                $raw = whois_lookup($normalized['ascii_domain']);
                $parsed = parse_whois_result($raw);
                return [
                    'input' => $inputString,
                    'domain' => $normalized['display_domain'],
                    'status' => $parsed['status'],
                    'available' => $parsed['available'],
                    'premiumScore' => $premium['score'],
                    'premiumTier' => $premium['tier'],
                    'note' => $parsed['note'] ?? null,
                ];
            } catch (Throwable $socketError) {
                return [
                    'input' => $inputString,
                    'domain' => $normalized['display_domain'],
                    'status' => 'error',
                    'available' => null,
                    'premiumScore' => $premium['score'],
                    'premiumTier' => $premium['tier'],
                    'note' => 'HTTPS შეცდომა: ' . $error->getMessage() . '; WHOIS fallback შეცდომა: ' . $socketError->getMessage(),
                ];
            }
        }

        return [
            'input' => $inputString,
            'domain' => $normalized['display_domain'],
            'status' => 'error',
            'available' => null,
            'premiumScore' => $premium['score'],
            'premiumTier' => $premium['tier'],
            'note' => 'Lookup შეცდომა: ' . $error->getMessage(),
        ];
    }
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    json_response(405, ['error' => 'Method Not Allowed']);
}

$rawBody = file_get_contents('php://input');
$body = json_decode((string) $rawBody, true);
if (!is_array($body)) {
    json_response(400, ['error' => 'Invalid JSON body.']);
}

$domains = $body['domains'] ?? [];
if (!is_array($domains) || count($domains) === 0) {
    json_response(400, ['error' => 'დომენების სია ცარიელია.']);
}

if (count($domains) > 300) {
    json_response(400, ['error' => 'ერთ ჯერზე მაქსიმუმ 300 დომენი გადაამოწმე.']);
}

$results = [];
foreach ($domains as $item) {
    $results[] = check_single_domain($item);
}

$summary = ['available' => 0, 'taken' => 0, 'unknown' => 0, 'invalid' => 0, 'error' => 0];
foreach ($results as $item) {
    $status = $item['status'] ?? 'unknown';
    if (!array_key_exists($status, $summary)) {
        $summary[$status] = 0;
    }
    $summary[$status] += 1;
}

json_response(200, [
    'checkedAt' => gmdate('c'),
    'summary' => $summary,
    'results' => $results,
]);
