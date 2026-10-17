# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = "eu4dialogue/pm/mock-data"

# 8. MOCK 08: Indicator Performance Tracking Table (IPTT) - EU/UNDP Standard
iptt_data = """Indicator_Code,Result_Level,Indicator_Statement,Disaggregation,Baseline_Value,Year1_Target,Q1_Target,Q1_Actual,Q2_Target,Q2_Actual,Q3_Target,Q3_Actual,Cumulative_Actual,Achievement_Rate_Percent,RAG_Status,Means_of_Verification,Responsible_Lead
IND-IMP-01,Impact,"Increased trust and social cohesion among conflict-affected communities",Gender / Age / Location,32.5%,55.0%,N/A,N/A,N/A,N/A,48.0%,46.5%,46.5%,84.5%,Green,Independent Annual Perception Survey,M&E Specialist
IND-OUT-01,Outcome 1,"Number of joint community peacebuilding initiatives implemented by local CSOs",Municipality (Gori/Zugdidi),0,8,1,1,3,2,6,5,5,83.3%,Amber,Initiative Completion Reports & MOUs,Project Coordinator
IND-OUT-02,Outcome 2,"Percentage of targeted youth demonstrating enhanced conflict-resolution skills",Gender (F/M),24.0%,70.0%,35.0%,38.0%,55.0%,52.0%,70.0%,68.0%,68.0%,97.1%,Green,Pre/Post Assessment Survey Analysis,M&E Specialist
IND-OUT-03,Outcome 3,"Number of local women leaders actively participating in municipal dialogue tables",Age / IDP Status,12,40,15,14,28,24,40,36,36,90.0%,Green,Municipal Meeting Minutes & Sign-in Sheets,Gender Officer
IND-OUTP-1.1,Output 1.1,"Number of grassroots dialogue workshops and community forums conducted",Region / Theme,0,12,3,3,7,6,10,10,10,100.0%,Green,Workshop Agendas & Participant Registers,Facilitator Lead
IND-OUTP-1.2,Output 1.2,"Number of vulnerable community members reached through dialogue roundtables",Gender / Vulnerability,0,250,60,65,140,125,200,195,195,97.5%,Green,Signed Attendance Logs & Photo Documentation,Field Assistant
IND-OUTP-2.1,Output 2.1,"Number of youth enrolled in civic tech & AI-driven peacebuilding hackathons",Gender (F/M),0,80,20,22,50,45,80,68,68,85.0%,Amber,Hackathon Registration Database,Youth Coordinator
IND-OUTP-2.2,Output 2.2,"Number of prototype community problem-solving digital solutions developed",Domain (Civic/Env/Social),0,6,1,1,3,2,5,4,4,80.0%,Amber,Prototype Repositories & Demo Decks,Tech Facilitator
IND-OUTP-3.1,Output 3.1,"Number of women-led social micro-enterprises receiving technical mentorship",Economic Sector,0,15,4,4,10,8,15,12,12,80.0%,Amber,Mentorship Logs & Business Plans,Livelihoods Lead
IND-OUTP-3.2,Output 3.2,"Number of cross-boundary agricultural and trade dialogue sessions held",Sector (Agri/Water),0,4,1,0,2,1,3,1,1,33.3%,Red,Meeting Protocols & Formal Minutes,Senior Liaison
IND-OUTP-4.1,Output 4.1,"Number of bilingual peacebuilding and social cohesion policy briefs published",Language (KA/EN),0,3,1,1,2,2,3,3,100.0%,Green,Published Briefs & Distribution Records,Communications Officer
IND-OUTP-4.2,Output 4.2,"Number of local media and community podcast episodes produced and disseminated",Channel / Platform,0,8,2,2,5,5,8,9,112.5%,Green,Broadcast Links & Digital Analytics Logs,Media Specialist
"""

with open(os.path.join(base_dir, "mock_08_iptt_indicator_tracking_table.csv"), "w", encoding="utf-8") as f:
    f.write(iptt_data.strip() + "\n")

print("Created mock_08_iptt_indicator_tracking_table.csv")

# 9. MOCK 09: Qualitative Most Significant Change (MSC) Interviews
msc_data = """=== EU4Dialogue Project: Qualitative M&E - Most Significant Change (MSC) Case Studies ===
Methodology: Most Significant Change (MSC) & Thematic Qualitative Evaluation
Target Area: Shida Kartli & Samegrelo Conflict-Affected Communities
Date: Q3 Monitoring Cycle, October 2026
Format: Field Interviews & Thematic Story Transcripts

---

[STORY 01: Youth Civic Empowerment & Conflict Transformation]
რესპონდენტი: მარიამ ლ. (22 წლის, სტუდენტი, გორის მუნიციპალიტეტის გამყოფი ხაზის სოფელი)
ინტერვიუერი: M&E საველე ოფიცერი
კითხვა: "რა იყო ყველაზე მნიშვნელოვანი ცვლილება, რაც პირადად თქვენთვის და თქვენი თანასოფლელებისთვის მოხდა ამ პროექტის დაწყების შემდეგ?"
მარიამის პასუხი:
"ყველაზე დიდი ცვლილება ის არის, რომ სოფელში უიმედობის და იზოლაციის განცდა გაქრა. აქამდე ახალგაზრდებს ეგონათ, რომ ჩვენი ხმა არავის აინტერესებდა. ჰაკათონის და დიალოგის ვორქშოპების შემდეგ ჩვენ შევქმენით ახალგაზრდული სათემო საბჭო. ადრე თუ გოგონებს ერიდებოდათ საჯარო შეხვედრებზე აზრის გამოთქმა, ახლა ჩვენი პროექტის ფარგლებში შექმნილ მობილურ აპლიკაციას (სათემო პრობლემების რუკას) თავად წარვადგენთ მუნიციპალიტეტის გამგეობაში. როცა მერმა ჩვენი იდეის საფუძველზე სოფლის განათების საკითხი მოაგვარა, მაშინ ვიგრძენით, რომ რეალური ძალა გვაქვს. მშვიდობა ჩვენთვის სწორედ ეს არის: როცა შენს მომავალს თავად მართავ და აღარ გრძნობ თავს მიტოვებულად."
ძირითადი თემები: ახალგაზრდული ლიდერობა, გოგონების ემპაუერმენტი, სათემო ადვოკატირება, იმედის დაბრუნება.

---

[STORY 02: Women's Economic Resilience & Social Cohesion]
რესპონდენტი: ქეთევან ჯ. (47 წლის, იძულებით გადაადგილებული პირი, მეწარმე, წალენჯიხის მუნიციპალიტეტი)
ინტერვიუერი: გენდერისა და მონიტორინგის კონსულტანტი
კითხვა: "როგორ შეცვალა პროექტში მონაწილეობამ თქვენი ოჯახისა და თემის ყოველდღიურობა?"
ქეთევანის პასუხი:
"დევნილთა დასახლებაში ქალების უმრავლესობა მხოლოდ შემწეობის მოლოდინში იყო. მენტორინგის პროგრამამ დამანახა, რომ ჩვენი ტრადიციული ხელსაქმე და ჩირის წარმოება შეიძლება შემოსავლიან საქმედ იქცეს. პროექტის დახმარებით შევქმენით ქალთა სასოფლო-სამეურნეო კოოპერატივი. ყველაზე მნიშვნელოვანი ცვლილება ეკონომიკურ შემოსავალზე მეტად ის იყო, რომ დასახლებისა და ადგილობრივი სოფლის ქალები, რომლებიც წლების განმავლობაში ერთმანეთს უნდობლად უყურებდნენ, ერთად დავსხედით საერთო სახელოსნოში. საერთო საქმემ გააქრო გაუცხოება. ახლა ერთმანეთს ჭირსა და ლხინში გვერდში ვუდგავართ."
ძირითადი თემები: ეკონომიკური დამოუკიდებლობა, დევნილთა ინტეგრაცია, ნდობის აღდგენა, ქალთა კოოპერაცია.

---

[STORY 03: Water Sharing & Cross-Community Pragmatic Peacebuilding]
რესპონდენტი: ავთანდილ მ. (61 წლის, ფერმერი, კასპის მუნიციპალიტეტი)
ინტერვიუერი: M&E კოორდინატორი
კითხვა: "რა იყო პროექტის ყველაზე ხელშესახები შედეგი თქვენს სოფელში?"
ავთანდილის პასუხი:
"ჩვენთან ყველაზე მტკივნეული იყო სარწყავი წყლის განაწილება მეზობელ ორ თემს შორის. ზაფხულობით საქმე ჩხუბამდე და პოლიციამდე მიდიოდა. პროექტის ფასილიტატორებმა შეგვახვედრეს ორივე მხარის უხუცესები და ფერმერები. თავიდან მძიმე საუბარი იყო, მაგრამ როცა დავთვალეთ, რამდენ მოსავალს ვკარგავდით დაპირისპირების გამო, შევთანხმდით წყლის გრაფიკზე და გავწმინდეთ სათავე ნაგებობა. ყველაზე დიდი ცვლილება ის არის, რომ წელს პირველად არცერთი ინციდენტი არ მომხდარა. მშვიდობა მაშინ არის მყარი, როცა საერთო სარგებელი გაკავშირებს."
ძირითადი თემები: რესურსების ერთობლივი მართვა, პრაგმატული მშვიდობა, კონფლიქტის დეესკალაცია.

---

[STORY 04: Local Media & Changing Narrative]
რესპონდენტი: თორნიკე გ. (29 წლის, რეგიონული ჟურნალისტი და პოდკასტერი, ზუგდიდი)
ინტერვიუერი: კომუნიკაციებისა და M&E სპეციალისტი
კითხვა: "როგორ იმოქმედა პროექტმა მედია გაშუქებასა და კონფლიქტის ნარატივზე?"
თორნიკეს პასუხი:
"რეგიონული მედია ადრე კონფლიქტის თემას მხოლოდ სენსაციურად, დაძაბულობისა და მტრობის კონტექსტში აშუქებდა. პროექტის ტრენინგებმა და მცირე საგრანტო მხარდაჭერამ მოგვცა შესაძლებლობა, გაგვეკეთებინა პოდკასტების სერია ადამიანურ ისტორიებზე: როგორ ეხმარებიან ექიმები ერთმანეთს, როგორ ვაჭრობენ ადამიანები და როგორ ინარჩუნებენ ნათესაურ კავშირებს. როცა პოდკასტმა 50,000-ზე მეტი ნახვა დააგროვა და კომენტარებში ხალხმა მადლობა დაგვიწერა ობიექტურობისთვის, მივხვდით, რომ საზოგადოებას მშვიდობის პოზიტიური დღის წესრიგი სჭირდება."
ძირითადი თემები: კონფლიქტ-სენსიტიური ჟურნალისტიკა, პოზიტიური მშვიდობის ნარატივი, საზოგადოებრივი აღქმა.

---

ინსტრუქცია M&E დავალებისთვის (Hands-on Qualitative M&E Lab):
1. AI Qualitative Coding: ატვირთეთ ეს ტექსტი Claude-ში ან NotebookLM-ში. გაუშვით პრომპტი თემატური კოდირებისთვის (Thematic Coding):
   - გამოყავით 4 მთავარი ტრანსფორმაციული თემა (Themes of Change);
   - ჩაატარეთ ბენეფიციართა განწყობის ანალიზი (Sentiment & Perception Shift);
   - ამოიღეთ დაუგეგმავი/გაუთვალისწინებელი პოზიტიური ეფექტები (Unintended Outcomes).
2. Human Interest Story დონორისთვის: შეარჩიეთ ერთი ისტორია და AI-ის დახმარებით გადააქციეთ EU/UNDP სტანდარტის 1-გვერდიან საილუსტრაციო ქეისად (Problem -> Action -> Tangible Impact -> Direct Quote -> Photo Placeholder).
"""

with open(os.path.join(base_dir, "mock_09_qualitative_msc_interviews.txt"), "w", encoding="utf-8") as f:
    f.write(msc_data.strip() + "\n")

print("Created mock_09_qualitative_msc_interviews.txt")
