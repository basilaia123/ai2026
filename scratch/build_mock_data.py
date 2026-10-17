# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = "eu4dialogue/pm/mock-data"
os.makedirs(base_dir, exist_ok=True)

# 1. MOCK 01: Pre/Post Survey Responses (Julius AI - M&E Analytics)
survey_rows = [
    "Participant_ID,Age_Group,Gender,Municipality,Target_Group,Pre_Knowledge_Score_1_to_5,Post_Knowledge_Score_1_to_5,Pre_Confidence_Score_1_to_5,Post_Confidence_Score_1_to_5,Satisfaction_Score_1_to_10,NPS_Category"
]

import random
random.seed(42)

municipalities = ["Gori", "Zugdidi", "Marneuli", "Kaspi", "Tsalka", "Akhalgori_Border_Zone", "Tsalenjikha"]
target_groups = ["Youth_Activists", "Women_Peacebuilders", "Community_Leaders", "Local_NGO_Staff", "IDP_Entrepreneurs"]
genders = ["Female", "Male", "Other_Prefer_Not_Say"]
age_groups = ["18-24", "25-34", "35-49", "50+"]

for i in range(1, 65):
    pid = f"RESP-{i:03d}"
    mun = random.choice(municipalities)
    tg = random.choice(target_groups)
    gen = random.choices(genders, weights=[0.55, 0.40, 0.05])[0]
    ag = random.choices(age_groups, weights=[0.35, 0.35, 0.20, 0.10])[0]
    
    pre_k = random.choices([1, 2, 3], weights=[0.3, 0.5, 0.2])[0]
    post_k = random.choices([4, 5], weights=[0.4, 0.6])[0]
    
    pre_c = random.choices([1, 2, 3], weights=[0.4, 0.4, 0.2])[0]
    post_c = random.choices([4, 5], weights=[0.35, 0.65])[0]
    
    sat = random.choices([8, 9, 10], weights=[0.2, 0.4, 0.4])[0]
    nps = "Promoter" if sat >= 9 else ("Passive" if sat >= 7 else "Detractor")
    
    survey_rows.append(f"{pid},{ag},{gen},{mun},{tg},{pre_k},{post_k},{pre_c},{post_c},{sat},{nps}")

with open(os.path.join(base_dir, "mock_01_pre_post_survey_responses.csv"), "w", encoding="utf-8") as f:
    f.write("\n".join(survey_rows) + "\n")

print("Created mock_01_pre_post_survey_responses.csv")

# 2. MOCK 02: Grant Budget Variance (Julius AI - Financial Audit & M&E)
budget_data = """Budget_Line_Code,Cost_Category,Description,Planned_Units,Actual_Units,Variance_Units,Variance_Percentage,Risk_Status,Donor_Approval_Needed
1.1,Personnel,Project Director (10 Months),12000,12000,0,0.0%,Normal,No
1.2,Personnel,Senior M&E Specialist (10 Months),8500,8500,0,0.0%,Normal,No
1.3,Personnel,Community Dialogue Facilitator,6000,6000,0,0.0%,Normal,No
2.1,Activities,5 Community Dialogue Roundtables (Gori & Zugdidi),4500,4100,-400,-8.9%,Normal,No
2.2,Activities,Youth Peacebuilding Hackathon & Bootcamp,7200,8100,+900,+12.5%,High_Variance,Yes
2.3,Activities,Women Community Leaders Mentoring Sessions,3800,3800,0,0.0%,Normal,No
3.1,Logistics,Field Transportation & Fuel for Regional Visits,2900,3450,+550,+19.0%,Critical_Variance,Yes
3.2,Logistics,Venue Catering & Accessible Meeting Space,3100,2950,-150,-4.8%,Normal,No
4.1,Visibility,Peacebuilding Policy Briefs Publication (Bilingual),2200,2200,0,0.0%,Normal,No
4.2,Visibility,Digital Video Stories & Social Media Campaign,3500,3100,-400,-11.4%,Normal,No
5.1,Evaluation,External Midterm Evaluation & Audit,4000,4000,0,0.0%,Normal,No
5.2,Evaluation,Final Independent Beneficiary Assessment,4500,4500,0,0.0%,Normal,No
6.1,Contingency,Unforeseen Field Logistics & Incident Buffer,2000,800,-1200,-60.0%,Normal,No
"""

with open(os.path.join(base_dir, "mock_02_grant_budget_variance.csv"), "w", encoding="utf-8") as f:
    f.write(budget_data.strip() + "\n")

print("Created mock_02_grant_budget_variance.csv")

# 3. MOCK 03: Field Interviews Raw (Module 6 - Donor Reporting & Synthesis)
interviews_data = """=== EU4Dialogue Project: Field Monitoring Interview Transcripts ===
Location: Shida Kartli, Conflict-Affected Administrative Boundary Zone
Date: October 2026
Format: Whisper Audio Transcription (Raw Text)

[INTERVIEW 01: Local Youth Initiative Leader]
დრო: 00:02:15 - 00:08:40
რესპონდენტი: სათემო ახალგაზრდული კლუბის კოორდინატორი
ციტატა: "ჩვენს სოფელში ახალგაზრდებს არ ჰქონდათ არანაირი სივრცე, სადაც ერთმანეთს შეხვდებოდნენ და რაიმე საერთო ინიციატივაზე იმსჯელებდნენ. საგრანტო პროექტის ფარგლებში შექმნილმა ჰაბმა პირველად მისცა მათ საშუალება, რომ დიალოგის ფორმატში ესაუბრათ ადგილობრივ პრობლემებზე: განათლების დეფიციტზე, უმუშევრობასა და იზოლაციაზე. განსაკუთრებით მნიშვნელოვანი იყო ის, რომ გოგონების ჩართულობა 60%-ზე ავიდა. ადრე მშობლებს ეშინოდათ მათი საღამოს შეხვედრებზე გამოშვება, მაგრამ როცა ნახეს უსაფრთხო გარემო და შედეგები, ნდობა გაიზარდა. მთავარი გამოწვევა ახლა არის ტრანსპორტი მეზობელი სოფლებიდან, რადგან საღამოს საზოგადოებრივი ტრანსპორტი არ მოძრაობს."

[INTERVIEW 02: Community Elder & Local Farmer]
დრო: 00:10:05 - 00:15:30
რესპონდენტი: ადგილობრივი მოსახლე, ასაკოვანი ფერმერი
ციტატა: "დიალოგი მაშინ არის ნამდვილი, როცა წყლის და მიწის პრობლემას ერთად წყვეტ. წლების განმავლობაში გამყოფი ხაზის სიახლოვეს სარწყავი წყლის არხები გაჭედილი იყო და მეზობელ თემებს შორის ყოველ ზაფხულს ჩხუბი მოსდიოდათ. პროექტის ფარგლებში გამართულმა სამუშაო შეხვედრებმა დაგვანახა, რომ ერთმანეთთან დაპირისპირებით ორივე მხარე ზარალდებოდა. შევქმენით წყლის მომხმარებელთა საერთო კომიტეტი. ახლა გრაფიკს ერთად ვადგენთ. ეს მშვიდობა ჩვენთვის კონკრეტული სარგებელია: მოსავალი აღარ გვიხმება და სოფელში დაძაბულობა აღარ არის."

[INTERVIEW 03: Women Entrepreneurs Representative]
დრო: 00:17:20 - 00:23:10
რესპონდენტი: ქალთა კოოპერატივის წევრი
ციტატა: "ქალებისთვის ეკონომიკური დამოუკიდებლობა არის მშვიდობის საფუძველი. როცა საკუთარი შემოსავალი გაქვს, ოჯახშიც და თემშიც შენი ხმა ისმის. ტრენინგებმა მოგვცა უნარები, თუ როგორ გავიტანოთ ადგილობრივი ჩირისა და თაფლის პროდუქცია რეგიონულ ბაზარზე ციფრული არხებით. თუმცა გვჭირდება მეტი მხარდაჭერა ლოჯისტიკაში და შეფუთვაში. თუ დონორი გააგრძელებს მეორე ეტაპს, აუცილებელია ქალთა ლიდერობის გაძლიერება ადგილობრივ გადაწყვეტილებების მიღებაში."

ინსტრუქცია მონაწილეებისთვის:
ამ ნედლი ინტერვიუებიდან AI-ის (Claude / GPT / NotebookLM) დახმარებით მოამზადეთ ოფიციალური დონორული რეპორტის ნარატიული სექცია:
1. Community Level Impact (მიღწეული შედეგები და გავლენა თემზე)
2. Direct Quotes Box (2 საუკეთესო ციტატა დონორისთვის)
3. Challenges & Corrective Actions (იდენტიფიცირებული გამოწვევები: ტრანსპორტი, ლოჯისტიკა და გადაჭრის გზები).
"""

with open(os.path.join(base_dir, "mock_03_field_interviews_raw.txt"), "w", encoding="utf-8") as f:
    f.write(interviews_data.strip() + "\n")

print("Created mock_03_field_interviews_raw.txt")

# 4. MOCK 04: Donor Guidelines Excerpt (Module 6 - Reflection Translation & NotebookLM)
guidelines_data = """=== EU4Dialogue Call for Proposals: Official Guidelines Excerpt ===
Donor: European Union / UNDP Partnership
Lot: Confidence Building, Local Development, and People-to-People Contacts

SECTION 1.2: MANDATORY CROSS-CUTTING PRINCIPLES

1. Do No Harm and Conflict Sensitivity:
All actions funded under this Call must strictly adhere to the 'Do No Harm' principle. Project interventions must be designed and implemented in a manner that avoids inadvertently exacerbating local tensions, deepening socio-economic divides, or exposing vulnerable conflict-affected populations to security or reputational risks. Applicants must conduct continuous conflict-sensitive risk assessments and demonstrate an adaptive management strategy.

2. Gender Equality and Social Inclusion (GESI):
Proposals must go beyond superficial participation metrics and incorporate gender-responsive programming. Projects must demonstrate how gender analysis informed the problem statement, baseline indicators, and activity design. Target groups must explicitly include women, vulnerable youth, and persons with disabilities. All monitoring indicators must be sex-disaggregated and accompanied by qualitative impact benchmarks.

3. Protection of Personal Data and Participant Anonymity:
In compliance with international data privacy standards and local security realities, applicants are prohibited from transmitting identifiable personal data (PII) of beneficiaries in public reports or unencrypted digital channels. Field documentation, human interest stories, and case studies must utilize anonymized pseudonyms or beneficiary coding.

SECTION 2.1: DELIVERABLES AND REPORTING STANDARDS
Interim and Final Narrative Reports must directly align with the approved Logical Framework (Logframe). Beneficiary progress must be evidenced through documented Means of Verification (MoV), including pre- and post-assessment surveys, attendance registers, and verified community dialogue protocols. Any budgetary variance exceeding 10% across budget categories requires prior formal written approval from the Contracting Authority.

ინსტრუქცია მონაწილეებისთვის:
1. ატვირთეთ ეს ტექსტი Google NotebookLM-ში, როგორც პირველადი დონორული წყარო.
2. გამოსცადეთ Reflection Translation მეთოდი Claude-ში:
   - ეტაპი 1: პირველადი სამუშაო თარგმანი ქართულად.
   - ეტაპი 2: კრიტიკული რეფლექსია დონორული ტერმინოლოგიის (Do No Harm, GESI, PII, Logframe, MoV) დაცვის შესამოწმებლად.
   - ეტაპი 3: საბოლოო დახვეწილი საორგანიზაციო ვერსიის მიღება.
"""

with open(os.path.join(base_dir, "mock_04_donor_guidelines_excerpt.txt"), "w", encoding="utf-8") as f:
    f.write(guidelines_data.strip() + "\n")

print("Created mock_04_donor_guidelines_excerpt.txt")

# 5. MOCK 05: Sensitive Field Report Raw (Module 7 - PII Anonymization & Do No Harm)
sensitive_data = """=== საველე მონიტორინგის ანგარიში: რისკის ქვეშ მყოფი ბენეფიციარების საქმეები ===
⚠️ სიმულაციური სასწავლო დოკუმენტი (მოდული 7): ტექსტი შეიცავს გამოგონილ პერსონალურ მონაცემებს (PII).
დავალება: გამოიყენეთ სისტემური პრომპტი და AI-ის დახმარებით ჩაატარეთ ტექსტის სრული ანონიმიზაცია და დე-იდენტიფიკაცია Do No Harm სტანდარტის მიხედვით.

ვიზიტის თარიღი: 12 ოქტომბერი, 2026
მონიტორი: ლევან მაისურაძე (პროექტის ასისტენტი, ტელ: +995 599 123456)
ადგილმდებარეობა: გორის მუნიციპალიტეტი, სოფელი ერგნეთი, მშვიდობის ქუჩა #14

ქეისი 1: მოწყვლადი ბენეფიციარის სოციალური შეფასება
ბენეფიციარი: ნინო გელაშვილი, დაბადებული 15.04.1982 წელს (პირადი ნომერი: 01024012345).
მისამართი: სოფელი ერგნეთი, მშვიდობის ქუჩა #14 (გამყოფი ხაზიდან 150 მეტრში).
საკონტაქტო ტელეფონი: +995 577 987654.
სტატუსი და დეტალები: ნინო არის იძულებით გადაადგილებული პირი (დევნილის მოწმობა #D-98124), მარტოხელა დედა სამ მცირეწლოვან შვილთან ერთად (ანა, 10 წლის; ლუკა, 8 წლის; დავითი, 5 წლის). ოჯახი იღებს სოციალურ შემწეობას (სარეიტინგო ქულა 45,200). ნინოს აწუხებს ქრონიკული ჰიპერტენზია და კონფლიქტის შემდგომი პოსტტრავმული სტრესული აშლილობა (PTSD), რის გამოც საჭიროებს მუდმივ მედიკამენტოზურ მხარდაჭერას.
პროექტში ჩართულობა: ნინომ გაიარა ქალთა მეწარმეობის სასათბურე მეურნეობის 3-დღიანი კურსი და მიიღო მცირე გრანტის ინვენტარი (წვეთოვანი სარწყავი სისტემა). მისი თქმით, მეზობელი სოფლის წარმომადგენლებთან შეხვედრამ მას დიდი იმედი მისცა, თუმცა უსაფრთხოების გამო ითხოვს, რომ მისი სახელი და ზუსტი საცხოვრებელი ადგილი არ გამოქვეყნდეს დონორის საჯარო ფეისბუქ პოსტებში.

ქეისი 2: ახალგაზრდა აქტივისტის უსაფრთხოების რისკები
ბენეფიციარი: დავით ქავთარაძე, 21 წლის (პირადი ნომერი: 59001098765).
საცხოვრებელი: სოფელი დიცი, რუსთაველის შესახვევი #7.
ტელეფონი: +995 598 456789, ელ-ფოსტა: dato.kavtaradze2005@gmail.com.
დეტალები: დავითი არის ადგილობრივი სტუდენტი, რომელიც მონაწილეობდა ახალგაზრდულ სამშვიდობო ჰაკათონში. ჰაკათონის ფარგლებში მან შექმნა ონლაინ პლატფორმა ახალგაზრდებს შორის დიალოგისთვის. ადგილობრივი უხუცესების ნაწილმა გამოთქვა ეჭვი მისი აქტივობების გამო. დავითი აცხადებს, რომ სოციალურ ქსელში მიიღო ანონიმური შეტყობინება გაფრთხილებით, რომ შეწყვიტოს თემის გარეთ ინფორმაციის გაცვლა.
მონიტორის რეკომენდაცია: დავითის მონაცემები სრულად უნდა დაიფაროს დონორის რეპორტში, რათა თავიდან ავიცილოთ ადგილობრივი კონფლიქტის ესკალაცია და მისი ოჯახის დისკრედიტაცია.

სავარჯიშოს მიზანი:
გადააკეთეთ ეს ტექსტი ისე, რომ:
1. ყველა სახელი, პირადი ნომერი, ტელეფონი, მეილი და ზუსტი მისამართი ჩანაცვლდეს კოდირებით (მაგ. [ბენეფიციარი ID-01, ქალი, 44 წლის, შიდა ქართლის სასაზღვრო სოფელი]).
2. სამედიცინო და ტრავმის დეტალები განზოგადდეს ისე, რომ დონორმა დაინახოს საჭიროება ბენეფიციარის იდენტიფიცირების გარეშე.
3. მონიტორის მონაცემები გასუფთავდეს.
"""

with open(os.path.join(base_dir, "mock_05_sensitive_field_report_raw.txt"), "w", encoding="utf-8") as f:
    f.write(sensitive_data.strip() + "\n")

print("Created mock_05_sensitive_field_report_raw.txt")

# 6. MOCK 06: Biased Project Narrative (Module 8 - Gender & Inclusive AI Audit)
biased_data = """=== საგრანტო განაცხადის სამუშაო მონახაზი: თემის განვითარების პროექტი ===
⚠️ სიმულაციური სასწავლო დოკუმენტი (მოდული 8): ტექსტი შეიცავს გაუცნობიერებელ გენდერულ და ასაკობრივ მიკერძოებას (Bias).
დავალება: ჩაატარეთ AI აუდიტი, გამოავლინეთ მიკერძოებული ფრაზები და გადაწერეთ ტექსტი Gender-Responsive და Inclusive AI სტანდარტების შესაბამისად.

პროექტის დასახელება: სოფლის აღორძინება და სათემო დიალოგის გაძლიერება
სამიზნე რეგიონი: სამეგრელო და შიდა ქართლი

პროექტის აღწერა (ნარატივი):
"პროექტის მთავარი მიზანია ადგილობრივი საზოგადოების გააქტიურება. ჩვენ ვგეგმავთ 100 ადგილობრივი მაცხოვრებლის გადამზადებას. პროექტის მართვისა და გადაწყვეტილების მიღების კომიტეტში მოვიწვევთ სოფლის თავკაცებს, ოჯახის უფროს მამაკაცებსა და გამოცდილ ფერმერებს, რადგან ტრადიციულად სწორედ მათ აქვთ რეალური გავლენა თემზე და შეუძლიათ სერიოზული გადაწყვეტილებების მიღება.

ქალბატონებისთვის სპეციალურად მოეწყობა ხელსაქმის, ქსოვისა და კულინარიული მასტერკლასები, რაც მათ საშუალებას მისცემს, სახლიდან გაუსვლელად დაეხმარონ ოჯახის ბიუჯეტს და არ მოწყდნენ საოჯახო საქმეებს. ასევე, ახალგაზრდებს დავავალებთ ღონისძიებების დროს სკამების დალაგებას, ტექნიკის აპარატურის გადატანას და სტუმრების მომსახურებას, რათა მათ ისწავლონ უფროსების პატივისცემა და შრომის ფასი.

რაც შეეხება შეზღუდული შესაძლებლობების მქონე პირებს, რადგან ჩვენი შეხვედრების დარბაზი მეორე სართულზეა და ლიფტი არ გვაქვს, მათთვის ინფორმაციას შემდგომში გადავცემთ მათი ოჯახის ჯანმრთელი წევრების მეშვეობით.

პროექტის ინდიკატორები:
- გადამზადებულია 100 ადამიანი;
- ჩატარებულია 10 შეხვედრა;
- გაზრდილია მოსახლეობის კმაყოფილება."

სავარჯიშოს მიზანი:
1. AI Bias Detection პრომპტით გამოავლინეთ 4 ძირითადი ეთიკური და გენდერული ხარვეზი ამ ტექსტში:
   - გენდერული როლების სტერეოტიპიზაცია (მამაკაცები როგორც ლიდერები, ქალები მხოლოდ კულინარიაში/სახლში);
   - ასაკობრივი მიკერძოება (ახალგაზრდები მხოლოდ როგორც მომსახურე პერსონალი);
   - ფიზიკური ბარიერი და დისკრიმინაცია შშმ პირთა მიმართ (მიუწვდომელი გარემო);
   - არა-სპეციფიკური, არა-დეზაგეგირებული ინდიკატორები (100 ადამიანი სქესის/ასაკის გარეშე).
2. გადაწერეთ ეს ნარატივი EU4Dialogue-ის ინკლუზიური და გენდერულად დაბალანსებული სტანდარტით.
"""

with open(os.path.join(base_dir, "mock_06_biased_project_narrative.txt"), "w", encoding="utf-8") as f:
    f.write(biased_data.strip() + "\n")

print("Created mock_06_biased_project_narrative.txt")

# 7. MOCK 07: Notion Grant Tasks CSV (Module 4 - Notion AI Grant Tracker Setup)
notion_tasks = """Task_Name,Phase,Assigned_Role,Start_Date,Due_Date,Status,Priority,Milestone_Flag
Kick-off Meeting with Donor Representatives,Inception,Project_Coordinator,2026-11-01,2026-11-03,Completed,High,Yes
Logframe and Indicators Final Baseline Audit,Inception,M&E_Specialist,2026-11-04,2026-11-10,Completed,High,Yes
Procurement of Workshop Equipment & Tablets,Logistics,Procurement_Officer,2026-11-10,2026-11-20,In_Progress,Medium,No
Drafting Pre-Assessment Questionnaire for Participants,Design,M&E_Specialist,2026-11-15,2026-11-22,In_Progress,High,No
Roundtable #1: Shida Kartli Youth Community Dialogue,Implementation,Facilitator_Youth,2026-12-01,2026-12-02,Not_Started,High,Yes
Roundtable #2: Samegrelo Women Peacebuilders Forum,Implementation,Facilitator_Women,2026-12-08,2026-12-09,Not_Started,High,Yes
Mid-term Expenditure Audit & Variance Check,Financial,Finance_Manager,2026-12-15,2026-12-20,Not_Started,Medium,No
Submission of Interim Narrative & Financial Report,Reporting,Project_Coordinator,2026-12-25,2026-12-30,Not_Started,Urgent,Yes
External Peer Evaluation & Beneficiary Feedback,Evaluation,External_Evaluator,2027-01-10,2027-01-20,Not_Started,Medium,No
Final Peacebuilding Pitch & Policy Presentation,Closure,Communications_Lead,2027-02-01,2027-02-05,Not_Started,High,Yes
"""

with open(os.path.join(base_dir, "mock_07_notion_grant_tasks.csv"), "w", encoding="utf-8") as f:
    f.write(notion_tasks.strip() + "\n")

print("Created mock_07_notion_grant_tasks.csv")
