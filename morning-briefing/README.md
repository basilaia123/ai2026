# დილის ბრიფინგი

სამუშაო დილით აგენტი კრებს სამ რამეს: დღის შეხვედრებს, წერილებს, რომლებზეც პასუხი შეიძლება დასჭირდეს, და ამინდს. მოდელი ამ მონაცემით წერს მოკლე ბრიფინგს. ფოსტა და კალენდარი მხოლოდ იკითხება.

აგენტი არც ერთ პროვაიდერზე არ არის მიბმული. მოდელი, ქალაქი, ფორმატი და გაგზავნის არხი `config.yaml`-შია. საიდუმლოებები `.env`-შია. კოდი მონაცემს თავად იღებს და მოდელს უგზავნის ჩვეულებრივ ტექსტად, ჩაშენებული tools-ის გარეშე.

## ფაილები

| გზა | როლი |
| --- | --- |
| `main.py` | დილის გაგზავნა, `--dry-run`, `--provider` |
| `bot.py` | Telegram ბოტი, long polling |
| `config.yaml` | მოდელების რიგი, ქალაქი, არხი, ლიმიტები, სისტემური პრომპტი |
| `.env` | მხოლოდ საიდუმლოებები (ნიმუში: `.env.example`) |
| `core/interfaces.py` | `LLMProvider`, `MailSource`, `CalendarSource`, `WeatherSource`, `Notifier` |
| `core/briefing.py` | `build_briefing`. ერთი წყაროს შეცდომა დანარჩენს არ აჩერებს |
| `providers/llm_litellm.py` | LiteLLM. სია ზემოდან ქვემოთ სცადებს |
| `sources/` | IMAP, CalDAV, ICS, Open-Meteo, ციტატა, ვალუტა |
| `notifiers/` | ფაილი, SMTP, Telegram გაგზავნა და `telegram_bot.py` |

ახალი წყარო ერთი ახალი ფაილია. კლასს სჭირდება `from_config(config, env)` და ინტერფეისის მეთოდი. შემდეგ `config.yaml`-ში იცვლება `module:Class` ხაზი.

## მოთხოვნები

- Python 3.11 ან უფრო ახალი
- ინტერნეტი გაშვებისას, თუ წყარო ჩართულია

## დაყენება

```bash
cd morning-briefing
python -m venv .venv
```

Linux და macOS:

```bash
. .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
chmod 600 .env
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

`.env`-ში `GEMINI_API_KEY` აუცილებელია, როცა მოდელი ჩართულია. ცარიელი გასაღები გაშვებას აჩერებს და არაფერს აგზავნის. `config.yaml`-ის `llm.models` სიაში პირველი ის მოდელია, რომელიც პირველი სცადება. სახელები LiteLLM-ის ფორმატით იწერება (`პროვაიდერი/მოდელი`) და მხოლოდ ამ ფაილში. თუ ყველა მოდელი ჩავარდა, ფაქტები მაინც იგზავნება, ბოლოს ეწერება `მოდელი მიუწვდომელია` და მოკლე მიზეზი. სრული შეცდომა რჩება ლოგში, გასაღების გარეშე. სიახლეები მაშინ სათაურებით და ბმულებით ჩანს, ციტატა კი ორიგინალით და შენიშვნით `(თარგმანი მიუწვდომელია)`.

ფოსტა Gmail-ია. `config.yaml`-ში უკვე წერია `imap.gmail.com` (პორტი 993, SSL) და `smtp.gmail.com` (პორტი 587, STARTTLS).

1. Gmail-ში გახსენი Settings, შემდეგ See all settings, Forwarding and POP/IMAP. მონიშნე Enable IMAP და შეინახე.
2. Google-ის ანგარიშში ჩართული უნდა იყოს 2-Step Verification. შემდეგ გახსენი [App Passwords](https://myaccount.google.com/apppasswords) და შექმენი პაროლი სახელით `morning-briefing`.
3. `.env`-ში ჩაწერე:

```env
IMAP_USERNAME=შენი@gmail.com
IMAP_PASSWORD=აბგდ ევზთ იკლმ ნოპრ
```

`IMAP_USERNAME` სრული Gmail მისამართია. `IMAP_PASSWORD` არის App Password, ჩვეულებრივი პაროლი კი არა. ოთხიან ჯგუფებს შორის დარჩენილ გამოტოვებებს პროგრამა თავად შლის.

აგენტი ყუთს `readonly` რეჟიმში ხსნის და `BODY.PEEK`-ით კითხულობს, ამიტომ წერილი წაკითხულად არ მოინიშნება.

თუ ბრიფინგიც იმავე ყუთში უნდა მოვიდეს, `config.yaml`-ში ჩაწერე `delivery.channel: email` და `.env`-ში `SMTP_TO=შენი@gmail.com`. `SMTP_USERNAME`, `SMTP_PASSWORD` და `SMTP_FROM` ცარიელი თუ დატოვე, პროგრამა გამოიყენებს IMAP-ის Gmail ანგარიშს.

კალენდრისთვის ნაგულისხმევია ICS ბმული (`ICS_URL`). CalDAV-ზე გადასვლა `config.yaml`-ში ერთი ხაზია:

```yaml
calendar:
  source: sources.calendar_caldav:CalDAVCalendarSource
```

ამინდს გასაღები არ სჭირდება. ქალაქი და კოორდინატები `weather` ბლოკშია.

## პირველი `--dry-run`

Dry-run ბეჭდავს ბრიფინგს და არაფერს აგზავნის. გაგზავნის არხის საიდუმლო ამ გაშვებას არ სჭირდება.

1. ზემოთ აღწერილი დაყენება და ერთი სამუშაო მოდელი `.env`-ში.
2. `config.yaml`-ში `llm.models`-ის პირველი ელემენტი დაუმთხვიე ამ მოდელს.
3. თუ ფოსტა და კალენდარი ჯერ არ გაქვს, ისინი ჩართული დატოვე. ჩავარდნილი ნაწილი ბრიფინგში დაიწერება როგორც `მიუწვდომელია`, დანარჩენი მაინც გავა. ამინდი გასაღების გარეშე უნდა ამოვიდეს.
4. გაუშვი:

```bash
python main.py --dry-run
```

კონკრეტული მოდელის იძულებით, სიის რიგის შეუცვლელად:

```bash
python main.py --dry-run --provider ollama_chat/qwen2.5
```

`--provider`-ის მნიშვნელობა ზუსტად ის სტრიქონია, რასაც LiteLLM ელოდება. ის კონფიგის სიას ამ ერთი გაშვებისთვის ანაცვლებს.

შედეგი ტერმინალში უნდა გამოჩნდეს. `out/briefing.txt` ამ რეჟიმში არ იქმნება.

ჩვეულებრივი გაშვება არხს `delivery.channel`-იდან იღებს (`file`, `email` ან `telegram`):

```bash
python main.py
```

`file` წერს `delivery.file_path`-ში. `email` იყენებს `smtp` ბლოკს და `SMTP_*` ცვლადებს. `telegram` იყენებს `TELEGRAM_BOT_TOKEN`-ს და `TELEGRAM_CHAT_ID`-ს.

## Telegram ბოტი

ბოტი იგივე წყაროებს ეკითხება, რასაც დილის გაგზავნა. ტოკენი და chat id ისევ `.env`-ის `TELEGRAM_BOT_TOKEN` და `TELEGRAM_CHAT_ID` ცვლადებია. ბოტი პასუხობს მხოლოდ ამ chat id-ს. სხვა ჩატიდან მოსული შეტყობინება არ იგზავნება და არ ლოგდება.

ბრძანებები:

- `/start` და `/help` აჩვენებს სიას და ღილაკებს. ღილაკი იმავე ფუნქციას იძახებს, რასაც ბრძანება.
- `/brief` აჩვენებს ამინდს, ციტატას, ფაქტს და ვალუტის კურსს
- `/weather` მხოლოდ ამინდს
- `/fx` მხოლოდ ვალუტის კურსს
- `/quote` მხოლოდ ციტატას და ფაქტს

ლოკალურად, იმავე საქაღალდიდან, სადაც `.env` დევს:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe bot.py
```

Linux-ზე:

```bash
. .venv/bin/activate
pip install -r requirements.txt
python bot.py
```

გაჩერება: Ctrl+C. ერთ დროს მხოლოდ ერთი `bot.py` უნდა მუშაობდეს, თორემ Telegram `getUpdates`-ზე კონფლიქტს აბრუნებს. დილის `main.py` ამას არ ეხება, ის მხოლოდ შეტყობინებას აგზავნის.

systemd სერვისი ბოტს ჩართვის შემდეგ თავად რესტარტავს.

`/etc/systemd/system/morning-briefing-bot.service`:

```ini
[Unit]
Description=Morning briefing Telegram bot
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory=/opt/morning-briefing
ExecStart=/opt/morning-briefing/.venv/bin/python /opt/morning-briefing/bot.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

ჩართვა:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now morning-briefing-bot.service
systemctl status morning-briefing-bot.service
```

`Restart=always` ნიშნავს, რომ პროცესის გაჩერების შემდეგ systemd თავიდან გაუშვებს, 5 წამის პაუზით.

## ტესტები

```bash
pip install -r requirements-dev.txt
python -m pytest
```

ტესტები ქსელს და ცოცხალ გასაღებს არ ეხებიან. წყაროები სატესტო ობიექტებითაა ჩანაცვლებული.

## ყოველ სამუშაო დილას

ძირითადი გზა თავად მანქანაა: Raspberry Pi, VPS ან სახლის კომპიუტერი. საათი მანქანის ადგილობრივი დროა. თბილისის დილისთვის სისტემის სარტყელი `Asia/Tbilisi` იყოს, ან cron-ის საათი გადაანაცვლე.

პროგრამა `.env`-ს თავად კითხულობს `main.py`-ის გვერდიდან, ამიტომ cron-ში ცვლადების ექსპორტი არ გჭირდება.

```cron
30 7 * * 1-5 /opt/morning-briefing/.venv/bin/python /opt/morning-briefing/main.py
```

`30 7 * * 1-5` ნიშნავს: წუთი 30, საათი 7, ყოველ თვეში, ყოველ დღეს, ორშაბათიდან პარასკევის ჩათვლით.

systemd timer იგივე გრაფიკს იძლევა, თუ cron არ გინდა.

`/etc/systemd/system/morning-briefing.service`:

```ini
[Unit]
Description=Morning briefing
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
WorkingDirectory=/opt/morning-briefing
ExecStart=/opt/morning-briefing/.venv/bin/python /opt/morning-briefing/main.py
```

`/etc/systemd/system/morning-briefing.timer`:

```ini
[Unit]
Description=Weekday morning briefing

[Timer]
OnCalendar=Mon..Fri 07:30:00
Persistent=true

[Install]
WantedBy=timers.target
```

ჩართვა:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now morning-briefing.timer
systemctl list-timers morning-briefing.timer
```

`Persistent=true` ნიშნავს, რომ თუ მანქანა 07:30-ზე გამორთული იყო, გაშვება ჩართვის შემდეგ ერთხელ მოხდება.

GitHub Actions ამ პროექტის გაშვების გზა არ არის. ფოსტა და კალენდარი იმ მანქანაზეა, სადაც საიდუმლოებები გიწევს.

## ქცევა, რომელსაც უნდა ელოდო

- მოდელების სიაში პირველის შეცდომა ან ცარიელი პასუხი შემდეგ მოდელზე გადადის. ლოგში ჩანს მოდელის სახელი და შეცდომის ტიპი, არა საიდუმლო.
- ფოსტა, კალენდარი და ამინდი ცალ-ცალკე ცდებიან. ჩავარდნილი ნაწილი არის `მიუწვდომელია`. გამორთული წყარო არის `გამორთულია`.
- წერილის ტექსტი მოდელისთვის მონაცემია. სისტემურ პრომპტში წერია, რომ შიგთავსის ინსტრუქციები არ შესრულდნენ.
- აგენტი წერილს არ აგზავნის, არ შლის და კალენდარს არ ცვლის. SMTP და Telegram მხოლოდ უკვე შედგენილ ბრიფინგს აგზავნიან, და მხოლოდ მაშინ, როცა `--dry-run` არ არის.
- ლოგი საიდუმლოს `***`-ით ფარავს. ბრიფინგის ტექსტი ლოგში არ იწერება.

## ლოგი

`logging.level` კონფიგშია (`INFO` ან `DEBUG`). `DEBUG` შეცდომის კვალს ბეჭდავს. გასაღები მაინც დაიფარება, თუ ის `.env`-ის მგრძნობიარე ცვლადშია.
