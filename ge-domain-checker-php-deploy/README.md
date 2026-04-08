# GE Domain Checker (PHP)

ეს არის `.ge` დომენების შემმოწმებელი აპის PHP ვერსია, რომელიც კარგად მუშაობს shared hosting/cPanel გარემოში.

## ფაილები

- `index.php` - მთავარი გვერდი
- `app.js` - UI ლოგიკა (გენერატორი, ფილტრი, export, ფავორიტები)
- `styles.css` - სტილები
- `api/check.php` - დომენის შემოწმების API (default: HTTPS RDAP lookup)

## ლოკალურად გაშვება (თუ PHP გაქვს დაყენებული)

```bash
php -S localhost:8080
```

შემდეგ გახსენი:

`http://localhost:8080/ge-domain-checker-php/`

## cPanel / Shared Hosting Deploy

1. `ge-domain-checker-php` ფოლდერის შიგთავსი ატვირთე `public_html`-ში (ან ქვე-ფოლდერში).
2. დარწმუნდი, რომ PHP ვერსია არის `8.0+` (სასურველია `8.1+`).
3. თუ ქვე-ფოლდერში დებ (მაგ. `/domains`), გახსენი: `https://yourdomain.ge/domains/`.
4. აპი იმუშავებს დამატებითი dependency-ის გარეშე.

## Lookup რეჟიმი

- პირველადი წყარო: `nic.ge` ძებნის გვერდი (`https://nic.ge/en/find?domain={domain}`) ტექსტური parser-ით.
- Default რეჟიმი: HTTPS lookup endpoint rotation:
  - `https://rdap.org/domain/{domain}`
  - `https://www.rdap.net/domain/{domain}`
- Endpoint-ების შეცვლა შეგიძლია `LOOKUP_ENDPOINTS` env-ით (comma-separated).
- NIC endpoint-ის override: `NIC_WEB_WHOIS_ENDPOINT`.
- ტრაფიკის დასათრგუნად გამოიყენება rate-limit delay (`LOOKUP_MIN_INTERVAL_MS`, default `1100`) და retry (`LOOKUP_MAX_RETRIES`, default `2`).
- თუ lookup `HTTP 404` აბრუნებს და DNS-ზე დელეგაცია არ ჩანს, შედეგი ითვლება `available`-ად (best-effort inference).
- optional fallback: თუ გინდა socket WHOIS fallback, დაამატე env:
  - `ENABLE_SOCKET_FALLBACK=1`
  - `WHOIS_HOST`, `WHOIS_PORT`, `WHOIS_TIMEOUT_MS`

## გენერატორის ოფცია

- იდეების გენერატორში ნაგულისხმევად სიმბოლოები/ციფრები გამორთულია.
- `რეჟიმი` dropdown-ით ირჩევ `მხოლოდ ასოები` ან `დეფისი + ციფრები`.
- დამატებით შენარჩუნებულია checkbox fallback.

## შედეგების სორტირება

- შედეგების ცხრილში არის `ქულის სორტირება`:
  - `მაღლიდან დაბლა`
  - `დაბლიდან მაღლა`

## Hosting შენიშვნა

- ახალი ვერსია აღარ არის დამოკიდებული მხოლოდ `port 43` WHOIS socket-ზე.
- თუ shared hosting-ზე socket-ები შეზღუდულია, default HTTPS რეჟიმი ჩვეულებრივ მუშაობს.
- თუ ჰოსტინგი მთლიან outbound HTTPS-საც ზღუდავს, დაუკავშირდი support-ს.
