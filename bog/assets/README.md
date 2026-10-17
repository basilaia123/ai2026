# საქართველოს ბანკი (BOG) · სასწავლო და სატესტო ფაილების კატალოგი
**პროექტი:** ხელოვნური ინტელექტის პრაქტიკული გამოყენება სამშენებლო-სარემონტო პროექტების მართვაში  
**აუდიტორია:** BOG უძრავი ქონების დეპარტამენტი, არქიტექტორები, პროექტების მენეჯერები (PM) და ტექნიკური ზედამხედველები  
**უსაფრთხოების სტანდარტი:** Zero-Retention პოლიტიკა · Traffic-Light მონაცემთა კლასიფიკაცია  
**სტრუქტურა:** 3 სესია · 12 სატესტო რესურსი

---

## 1. სატესტო ფაილების სრული რეესტრი (Asset Catalog)

### სესია 1: სისტემური პერსონები და მონაცემთა უსაფრთხოება
| ფაილი | ფორმატი | სამიზნე როლი / AI ინსტრუმენტი | დანიშნულება და შინაარსი | უსაფრთხოება |
| :--- | :--- | :--- | :--- | :--- |
| `session1/bog_architect_system_persona.txt` | TXT | არქიტექტორი · Claude / ChatGPT Project | Brand Book-ის, ესთეტიკის, მასალებისა და 41-ე დადგენილების საავტორო ზედამხედველობის სისტემური ინსტრუქცია. | 🟢 საჯარო |
| `session1/bog_pm_system_persona.txt` | TXT | Lead PM · Claude / ChatGPT Project | ვადების, ბიუჯეტის, რისკების, BOQ-ის, Fast-Tracking-ისა და სატენდერო გადაწყვეტილებების სისტემური ინსტრუქცია. | 🟢 საჯარო |
| `session1/bog_supervisor_system_persona.txt` | TXT | ტექზედამხედველი · Gemini Gem / Claude | სამშენებლო ნორმების, Snag List-ის, დეფექტების, ყოველდღიური საიტ-ოქმების და უსაფრთხოების სისტემური ინსტრუქცია. | 🟢 საჯარო |
| `session1/traffic_light_data_sanitization_guide.txt` | TXT | ყველა მონაწილე · Compliance Guide | შუქნიშნის პრინციპი (🟢 მწვანე, 🟡 ყვითელი, 🔴 წითელი), მასკირების წესები და Zero-Retention ჩეკლისტი. | 🟢 საჯარო |

---

### სესია 2: საველე ინსპექცია და ვიზუალური კონცეფციები
| ფაილი | ფორმატი | სამიზნე როლი / AI ინსტრუმენტი | დანიშნულება და შინაარსი | უსაფრთხოება |
| :--- | :--- | :--- | :--- | :--- |
| `session2/sample_field_voice_note_raw.txt` | TXT | ზედამხედველი / PM · ElevenLabs / Gemini | საველე ინსპექციის ნედლი აუდიო-ტრანსკრიპტი საიტ-ოქმის (Site Log) გენერირებისთვის. | 🟡 სამსახურებრივი |
| `session2/sample_defect_photos_manifest.txt` | TXT | ყველა როლი · Gemini 3.8 / Claude | 6 საკონტროლო დეფექტის დეტალური აღწერა (ბზარები, ჭერი, Lippage, პანდუსი, სერვერული, HVAC). | 🟡 სამსახურებრივი |
| `session2/sample_branch_interior_description.txt` | TXT | არქიტექტორი / PM · FLUX / Krea / Claude | Solo Lounge-ის ინტერიერის 7-ელემენტიანი ბაზისური ბლოკი 4-სურათიანი სერიის შესაქმნელად. | 🟢 საჯარო |
| `session2/gamma_status_presentation_prompt.txt` | TXT | Lead PM · Gamma 5 / Claude | 6-სლაიდიანი საოპერაციო პრეზენტაციის სტრუქტურირებული C.R.E.A.T.E. პრომპტი ტოპ-მენეჯმენტისთვის. | 🟡 სამსახურებრივი |
| `session2/sample-branch-interior.svg` | SVG | არქიტექტორი · Multimodal Vision / FLUX | ფილიალის ინტერიერის (Solo Lounge) ვექტორული ვიზუალიზაცია მულტიმოდალური ანალიზისთვის. | 🟢 საჯარო |
| `session2/sample-snag-defect-1.svg` | SVG | ზედამხედველი · Gemini 3.8 Flash Vision | კედლის ბზარის (Drywall joint crack, ~45 სმ) საინსპექციო ფოტო-იმიტაცია სახაზავითა და მანიშნებლებით. | 🟢 საჯარო |
| `session2/sample-snag-defect-2.svg` | SVG | ზედამხედველი · Gemini 3.8 Flash Vision | იატაკის ფილის სიმაღლეთა სხვაობისა (Lippage) და გატეხილი კუთხის საინსპექციო ფოტო-იმიტაცია. | 🟢 საჯარო |

---

### სესია 3: ნორმატიული ანალიტიკა, ტენდერები და პროექტის ჰაბი
| ფაილი | ფორმატი | სამიზნე როლი / AI ინსტრუმენტი | დანიშნულება და შინაარსი | უსაფრთხოება |
| :--- | :--- | :--- | :--- | :--- |
| `session3/decree_41_technical_regulations_excerpt.txt` | TXT | ყველა როლი · Gemini Notebook / Claude | საქართველოს მთავრობის 41-ე დადგენილების ოფიციალური ამონარიდი (საევაკუაციო კარის 90 სმ ნორმა). | 🟢 საჯარო |
| `session3/branch_x_boq_comparison_data.csv` | CSV | Lead PM / ზედამხედველი · Claude / ChatGPT | 8-პუნქტიანი სატენდერო BOQ ცხრილი (3 კონტრაქტორის ფასები, ვადები, მოცულობები, Red Flags). | 🟡 სამსახურებრივი |
| `session3/branch_x_drawing_explication.csv` | CSV | არქიტექტორი / PM · Gemini / Claude | ფილიალის ოთახების ექსპლიკაციის ცხრილი (160 მ², ფართობები, პერიმეტრები, კარები, დატვირთვა). | 🟡 სამსახურებრივი |
| `session3/site_coordination_meeting_transcript_oct08.txt` | TXT | Lead PM · Claude Sonnet 5.5 | 8 ოქტომბრის საკოორდინაციო თათბირის ნედლი ტრანსკრიპტი Smart Minutes-ისა და Catch-up-ისთვის. | 🟡 სამსახურებრივი |
| `session3/notion_project_hub_template.md` | MD | ყველა როლი · Notion / Obsidian | პროექტების მართვის ჰაბის სრული არქიტექტურა (4 მონაცემთა ბაზა, ხედები, დეშბორდები). | 🟡 სამსახურებრივი |

---

## 2. პრაქტიკული გამოყენების გზამკვლევი (Quick Start Guide)

### ნაბიჯი 1: სისტემური პერსონის გააქტიურება (სესია 1)
1. გახსენით **Claude** (Claude Projects) ან **ChatGPT Enterprise** (Custom GPT / Custom Instructions).
2. შექმენით ახალი პროექტი თქვენი როლის მიხედვით:
   - არქიტექტორებისთვის: გამოიყენეთ `bog_architect_system_persona.txt`
   - პროექტების მენეჯერებისთვის: გამოიყენეთ `bog_pm_system_persona.txt`
   - ზედამხედველებისთვის: გამოიყენეთ `bog_supervisor_system_persona.txt`
3. ჩასვით ფაილის შიგთავსი System Prompt-ის ან Instructions-ის ველში.

### ნაბიჯი 2: დეფექტების ამოცნობა და საიტ-ოქმი (სესია 2)
1. **Snag List-ის აწყობა:** ატვირთეთ `sample-snag-defect-1.svg` და `sample-snag-defect-2.svg` Gemini 3.8 Flash-ში (ან გამოიყენეთ `sample_defect_photos_manifest.txt`).
2. გაუშვით Snag List პრომპტი (რვეულის დავალება №1): მიიღეთ ცხრილი ლოკაციებით, სავარაუდო მიზეზითა და დარწმუნებულობის დონით.
3. **Voice-to-Report:** ჩასვით `sample_field_voice_note_raw.txt` თქვენს პერსონიფიცირებულ ასისტენტში და დააგენერირეთ დღის ოფიციალური საიტ-ოქმი.
4. **Gamma პრეზენტაცია:** დააკოპირეთ `gamma_status_presentation_prompt.txt` Gamma 5-ში და 2 წუთში მიიღეთ დასრულებული სლაიდები.

### ნაბიჯი 3: ტენდერები, ნორმები და კრიტიკული გზა (სესია 3)
1. **ნორმატიული კაზუსი:** ატვირთეთ `decree_41_technical_regulations_excerpt.txt` Gemini NotebookLM-ში ან Claude-ში და გადაამოწმეთ 85 სმ vs 90 სმ კარის საკითხი.
2. **BOQ Red Flags:** ატვირთეთ `branch_x_boq_comparison_data.csv` Claude Sonnet 5.5-ში (Extended Thinking რეჟიმში), გამოავლინეთ კონტრაქტორი A-ს +21% გაზრდილი მოცულობა და კონტრაქტორი B-ს სერტიფიკატების ნაკლებობა.
3. **Catch-up გრაფიკი:** ჩასვით `site_coordination_meeting_transcript_oct08.txt` და მიიღეთ ოფიციალური Smart Minutes და აღდგენითი გრაფიკი 6 ნოემბრისთვის.
4. **Notion Hub:** გადაიტანეთ `notion_project_hub_template.md` Notion-ში პროექტის სამუშაო სივრცის მყისიერად ასაწყობად.
================================================================================
