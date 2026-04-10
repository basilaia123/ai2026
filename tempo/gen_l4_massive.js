const fs = require('fs');
const pathSlides = 'c:\\Users\\GBASILAIA\\claude\\ai2026\\tempo\\lecture-4-slides.html';
const templatePath = 'c:\\Users\\GBASILAIA\\claude\\ai2026\\tempo\\skills\\tempo-course-generator\\assets\\slide-template.html';

let template = fs.readFileSync(templatePath, 'utf8');

const additionalTopics = [
    { title: "🎯 სესიის აჯენდა (180 წუთი)", icon: "🎯", content: "ბლოკი 1: ტექსტური კონტენტი (კალენდარი, ქეფშენები, PAS/AIDA).<br>ბლოკი 2: AI მულტიმედია (Midjourney, ElevenLabs, HeyGen)." },
    { title: "🧊 Icebreaker: კრეატიული ბლოკირება", icon: "🧊", isActivity: true, content: "დაწერეთ ჩატში, კონტენტის შექმნისას რა გიჭირთ ყველაზე მეტად? (იდეის მოფიქრება, ტექსტის დაწერა თუ ფოტოს პოვნა)." },
    { title: "⏳ ადრე vs ახლა (კონტენტ-მარკეტინგი)", icon: "⏳", content: "ტრადიციული 16 საათიანი მუშაობა vs AI-ის 1 საათიანი პროცესი. სტრატეგიიდან ვიზუალებამდე.", hasChart: true },
    { title: "📅 30-დღიანი კონტენტ-კალენდარი", icon: "📅", content: "ქაოტური პოსტები არ მუშაობს. Tempo-ს სჭირდება სტრატეგია, რომელიც აერთიანებს გაყიდვებს (Sales), საგანმანათლებლო (Educational) და ბრენდ-იმიჯის კონტენტს." },
    { title: "🗓️ კალენდრის პრომპტი", icon: "🗓️", desc: "ერთი პრომპტი მთელი თვის სტრატეგიისთვის.", isPrompt: true, content: "იმოქმედე როგორც Tempo Holding-ის Social Media სტრატეგმა.\nმიზანი: Queen's Residence-ის ბინების გაყიდვა.\nშეადგინე 30-დღიანი კალენდარი (კვირაში 3 პოსტი). ბალანსი: 40% გაყიდვები, 40% საგანმანათლებლო, 20% ბრენდი.\nფორმატი: ცხრილი 4 სვეტით (დღე | თემა | ვიზუალის იდეა | Hook)." },
    { title: "📝 პოსტის სტრუქტურა: PAS ფორმულა", icon: "📝", content: "PAS = Problem (პრობლემა), Agitation (გამწვავება), Solution (გამოსავალი). იდეალურია ინვესტორების 'ტკივილის წერტილებზე' (Pain points) სალაპარაკოდ." },
    { title: "✏️ PAS ფორმულის პრომპტი", icon: "✏️", desc: "ინვესტორებისთვის პრობლემაზე დაფუძნებული პოსტი.", isPrompt: true, content: "დაწერე პოსტი ინვესტორებისთვის PAS ფორმულით.\nპრობლემა: ინფლაცია ჭამს შენახულ ფულს.\nგამწვავება: ბანკში ფულის გაჩერება წამგებიანია.\nგამოსავალი: ინვესტირება Tempo-ს პრემიუმ უძრავ ქონებაში." },
    { title: "📝 პოსტის სტრუქტურა: AIDA ფორმულა", icon: "📝", content: "AIDA = Attention (ყურადღება), Interest (ინტერესი), Desire (სურვილი), Action (მოქმედება). კლასიკური სარეკლამო სტრუქტურა გაყიდვებისთვის." },
    { title: "✏️ AIDA ფორმულის პრომპტი", icon: "✏️", desc: "კლასიკური გაყიდვების პოსტის აწყობა.", isPrompt: true, content: "დაწერე Facebook პოსტი Serenade-ის პენტჰაუსებზე.\nაუდიტორია: ლოკალური VIP სეგმენტი. ტონი: ულტრა-პრემიუმ.\nგამოიყენე AIDA ფორმულა. \nგამოყავი ტექსტი აბზაცებად, მაქსიმუმ 3 ემაჯი. CTA: დარეგისტრირდი დახურულ ჩვენებაზე." },
    { title: "🪝 პირველი წინადადება (Hook)", icon: "🪝", content: "სოციალურ ქსელში მომხმარებელი სქროლავს სწრაფად. თუ პირველი წინადადება (Hook) არ არის დამრტყმელი, ტექსტს არავინ წაიკითხავს. AI გეხმარებათ 10 განსხვავებული Hook-ის გენერაციაში წამებში." },
    { title: "🪝 Hook-ების გენერაციის პრომპტი", icon: "🪝", desc: "10 სხვადასხვა ვარიანტის მიღება.", isPrompt: true, content: "მე მაქვს ეს პოსტი ბათუმის უძრავ ქონებაზე: [ტექსტი].\nდამიგენერირე 10 განსხვავებული, ძალიან 'დამრტყმელი' პირველი წინადადება (Hook) ამ პოსტისთვის.\nგამოიყენე სტატისტიკა, ინტრიგა ან პირდაპირი კითხვა." },
    { title: "🔄 ადაპტაცია ფორმატების მიხედვით", icon: "🔄", content: "სხვადასხვა პლატფორმას სხვადასხვა წესი აქვს. <b>LinkedIn</b> = პროფესიონალური (ROI, ინვესტიცია). <b>Instagram</b> = ესთეტიკა და ლაიფსტაილი. <b>Facebook</b> = საინფორმაციო/გასართობი." },
    { title: "🔄 პლატფორმის ადაპტაციის პრომპტი", icon: "🔄", desc: "ერთი ტექსტის ტრანსფორმაცია ქსელების მიხედვით.", isPrompt: true, content: "მე მაქვს ეს ტექსტი Facebook-ისთვის: [ტექსტი].\nგთხოვ გადააკეთო ის 2 ვერსიად:\n1. LinkedIn-ისთვის (უფრო ანალიტიკური, ციფრებზე და ROI-ზე ფოკუსით, ემაჯების გარეშე).\n2. Instagram-ისთვის (მოკლე, ესთეტიკური, Lifestyle ფოკუსით)." },
    { title: "🔥 აქტივობა: Roast My Post", icon: "🔥", isActivity: true, content: "განვიხილოთ ტიპური, ცუდი უძრავი ქონების პოსტი. 'იყიდება ბინა ბათუმში ულამაზესი ხედებით 🌊. იყიდე დღესვე და მიიღე ფასდაკლება. დარეკე 599123456 📞'. როგორ ვაქციოთ ეს პრემიუმ პოსტად? გაქვთ 1 წუთი ჩატში!" },
    { title: "🔍 გარჩევის კრიტერიუმები (Roast)", icon: "🔍", content: "C (კონტექსტი): იცის AI-მ, რომ პრემიუმ სეგმენტს ველაპარაკებით?<br>R (როლი): იცის რომ პრემიუმ ბროკერია?<br>T (ტონი): ხომ არ გამოვიდა იაფფასიანი 'გაყიდვების' ტექსტი?" },
    { title: "🎨 AI ვიზუალიზაცია (შესავალი)", icon: "🎨", content: "2026 წელს სტოკ-ფოტოების (Shutterstock) ეპოქა დასრულდა. Midjourney v6+ და FLUX ქმნიან ულტრა-რეალისტურ, პრემიუმ სურათებს, რომლებიც ნამდვილ ფოტოსესიას არ ჩამოუვარდება." },
    { title: "🛑 ვიზუალის გენერაციის მთავარი წესი", icon: "🛑", content: "არ სთხოვოთ AI-ს თქვენი კონკრეტული შენობის ზუსტი არქიტექტურის დახატვა რენდერის გარეშე. გამოიყენეთ AI <strong>Lifestyle-ის</strong>, ინტერიერის განწყობის და ემოციური, აბსტრაქტული ფოტოების შესაქმნელად." },
    { title: "📸 Claude-ის გამოყენება ფოტო-პრომპტისთვის", icon: "📸", content: "Midjourney და FLUX ინგლისურენოვან და სპეციფიკურ ფოტო-ტერმინოლოგიას (Lens, Lighting, Style) ითხოვს. უმჯობესია ფოტო-პრომპტი Claude-ს დააწერინოთ." },
    { title: "📸 ფოტო-პრომპტის გენერატორი", icon: "📸", desc: "Claude-ის პრომპტი Midjourney-ს ინსტრუქციის მისაღებად.", isPrompt: true, content: "მე მჭირდება ფოტოს გენერაცია Midjourney-ში ჩემი პოსტისთვის.\nპოსტის თემა: 'მშვიდი დილა საკუთარ პრემიუმ აპარტამენტში ბათუმში'.\nდამიწერე დეტალური პრომპტი ინგლისურად. აღწერე მთავარი ობიექტი, განათება (დილის მზე), ფონი და სტილი (Cinematic, photorealistic, 8k, architectural photography).\nმომაწოდე მხოლოდ ინგლისური პრომპტი." },
    { title: "🌟 FLUX მოდელის სპეციფიკა", icon: "🌟", content: "Midjourney-სგან განსხვავებით, FLUX ბევრად უკეთესად უმკლავდება <b>ტექსტის დაწერას უშუალოდ სურათზე</b> და რთული თითების/სახეების რეალისტურ გენერაციას." },
    { title: "🌟 FLUX პრომპტის მაგალითი ტექსტით", icon: "🌟", desc: "სურათზე ტექსტის ზუსტი განთავსება.", isPrompt: true, content: "A photorealistic image of a sleek, modern billboard on a premium street. The billboard clearly says 'TEMPO HOLDING' in bold, elegant gold serif letters on a black background. Cinematic lighting, high end real estate vibe." },
    { title: "💡 Image-to-Image ტექნიკა", icon: "💡", content: "თუ გსურთ, რომ AI-მ თქვენი რეალური ოთახის რენდერს დაადოს ახალი განათება ან ავეჯი, ატვირთეთ თქვენი ფოტო და გამოიყენეთ როგორც 'რეფერენსი' (Image weight)." },
    { title: "🎬 ვიდეო-კონტენტი (Reels, Shorts)", icon: "🎬", content: "ალგორითმები ორგანულ Reach-ს ძირითადად მოკლე ვიდეოებს (Reels/TikTok) აძლევენ. AI-ს შეუძლია ვიდეოს სრული სკრიპტირება წამებში." },
    { title: "🎬 ვიდეო სცენარის პრომპტი", icon: "🎬", desc: "15-წამიანი დინამიური სცენარი.", isPrompt: true, content: "დაწერე 15-წამიანი Instagram Reel-ის სცენარი თემაზე: 3 მიზეზი, რატომ არის Tempo-ში ინვესტირება დაცული.\nფორმატი: ცხრილი 3 სვეტით.\n1. წამები (მაგ: 0:00-0:03)\n2. ვიზუალი (რა ხდება ეკრანზე)\n3. Voiceover (რა ტექსტს ამბობს სპიკერი)." },
    { title: "🗣️ ElevenLabs - პრემიუმ აუდიო გენერაცია", icon: "🗣️", content: "ElevenLabs არის საუკეთესო Text-to-Speech ინსტრუმენტი 2026 წელს. შეგიძლიათ შეიყვანოთ Claude-ის დაწერილი ქართული/ინგლისური სკრიპტი და მიიღოთ პროფესიონალური გახმოვანება სრულიად რეალისტური ემოციური ტემბრით." },
    { title: "🗣️ Voice Cloning (ხმის კლონირება)", icon: "🗣️", content: "თქვენ შეგიძლიათ ატვირთოთ თქვენი (ან დირექტორის) ხმის 1-წუთიანი ჩანაწერი ElevenLabs-ში და AI მომავალში ნებისმიერ ტექსტს თქვენივე ხმით წაიკითხავს. იდეალურია პოდკასტებისა და Reels-ისთვის!" },
    { title: "👤 HeyGen / Synthesia (AI ვიდეო ავატარები)", icon: "👤", content: "თუ კამერის წინ დგომა არ გსურთ, HeyGen ქმნის რეალისტურ ციფრულ ადამიანს, რომელიც ტუჩების იდეალური სინქრონიზაციით კითხულობს თქვენს ტექსტს. იდეალურია უძრავი ქონების 'News Update' ვიდეოებისთვის." },
    { title: "♻️ Repurposing (კონტენტის გადამუშავება)", icon: "♻️", content: "ნუ შექმნით ახალ კონტენტს ყოველდღე. აიღეთ ერთი გრძელი YouTube ვიდეო ან ბლოგპოსტი და სთხოვეთ AI-ს, დაჭრას ის 5 მოკლე Reels სცენარად და 3 Facebook პოსტად." },
    { title: "♻️ Repurposing პრომპტი", icon: "♻️", desc: "ერთი ვიდეოს გარდაქმნა თვის კონტენტად.", isPrompt: true, content: "აქ არის ჩვენი დირექტორის ბოლო 20-წუთიანი ინტერვიუს ტრანსკრიპტი:\n[ტექსტი]\nგთხოვ, ამოიღო 3 ყველაზე საინტერესო ციტატა და თითოეული გადააქციო 15-წამიანი Reel-ის სცენარად (Hook + Body + CTA) ჩვენი სოციალური მედიისთვის." },
    { title: "📊 სოციალური მედიის მეტრიკები", icon: "📊", content: "AI დაგეხმარებათ გააანალიზოთ, რომელი პოსტი მუშაობს. გადმოწერეთ Facebook-ის წინა თვის რეპორტი ექსელში და ჩააგდეთ Claude-ში ანალიზისთვის." },
    { title: "📊 მეტრიკების ანალიზის პრომპტი", icon: "📊", desc: "მონაცემებზე დაფუძნებული ფიდბექი.", isPrompt: true, content: "მიმაგრებულია წინა თვის სოც. მედიის რეპორტი.\nგააანალიზე მონაცემები და მითხარი: 1. რომელი 3 პოსტი იყო ყველაზე წარმატებული Reach/Engagement-ით? 2. რა აქვთ ამ პოსტებს საერთო? 3. მომეცი 5 ახალი იდეა ამ ტრენდზე დაყრდნობით." },
    { title: "🧑‍✈️ აქტივობა: შტურმანი (Screen Takeover)", icon: "🧑‍✈️", isActivity: true, content: "მოხალისე აზიარებს ეკრანს. 5 წუთში Claude-ში ვქმნით Queen's Residence-ის 1 კვირის კალენდარს, ვირჩევთ 1 პოსტს, ვწერთ ტექსტს (AIDA) და ვწერთ ფოტო-პრომპტს Midjourney-სთვის." },
    { title: "🤝 გუნდური მუშაობა (Approvals)", icon: "🤝", content: "Notion-ის ბაზების დახმარებით შეგიძლიათ შექმნათ კონტენტ-კალენდარი, სადაც მარკეტერი აგდებს AI-ით დაწერილ პოსტს, ხოლო დირექტორი უბრალოდ აჭერს ღილაკს 'Approved' გამოსაქვეყნებლად." },
    { title: "🛠 Custom GPT-ები სოც. მედიისთვის", icon: "🛠", content: "შექმენით თქვენი 'Tempo Social Media Manager' GPT OpenAI-ში. აუტვირთეთ მას Tempo-ს ბრენდბუქი, წინა კარგი პოსტები და სტილის გაიდლაინი. ამის მერე მას აღარ დასჭირდება ტონის ხშირი მითითება." },
    { title: "📈 Case Study: სრული კამპანიის ლოგიკა", icon: "📈", content: "1. AI სტრატეგია (Claude) ➔ 2. ტექსტები (GPT/Claude) ➔ 3. ვიზუალი (FLUX) ➔ 4. აუდიო (ElevenLabs) ➔ 5. პოსტინგი. ეს არის 2026 წლის თანამედროვე 360-გრადუსიანი კამპანია." },
    { title: "✅ შეჯამება: 3 ოქროს წესი", icon: "✅", content: "1. სტრატეგია ჯერ (30-დღიანი კალენდარი).<br>2. ფორმატის ძალა (PAS/AIDA).<br>3. მულტიმედია (ტექსტი+ვიზუალი+აუდიო ერთიან სისტემაში)." },
    { title: "🚀 შემდეგი სესია", icon: "🚀", content: "მომავალ სესიაზე გადავალთ გაყიდვების სკრიპტებსა და Lead Generation-ის (ახალი კლიენტების მოზიდვის) ავტომატიზაციაზე Make.com-ის გამოყენებით!" }
];

let generatedHtml = '';
additionalTopics.forEach((t, idx) => {
    const slideNumber = idx + 1;
    let contentHtml = '';
    
    if (t.isActivity) {
        contentHtml = `
        <div class="mt-10 bg-tempo-900 border border-tempo-gold/30 rounded-xl overflow-hidden shadow-lg relative">
            <div class="absolute -right-6 -top-6 text-[8rem] opacity-5">${t.icon}</div>
            <div class="p-6 relative z-10 flex flex-col md:flex-row gap-6 items-center">
                <div class="w-16 h-16 rounded-full bg-tempo-gold/20 flex items-center justify-center text-3xl shrink-0 border border-tempo-gold/30">${t.icon}</div>
                <div class="text-white w-full">
                    <h4 class="text-tempo-gold font-bold text-xl mb-2" style="color: #C5A059 !important;">აქტივობა</h4>
                    <p class="text-sm text-gray-300 mb-3" style="color: #D1D5DB !important;">${t.content}</p>
                </div>
            </div>
        </div>`;
    } else if (t.hasChart) {
        contentHtml = `
        <p class="text-gray-700">${t.content}</p>
        <div class="mt-6 bg-white p-6 rounded-xl shadow-sm border border-gray-200">
            <canvas id="contentSavingsChart" style="max-height: 250px;"></canvas>
        </div>`;
    } else if (t.isPrompt) {
        contentHtml = `
        <p class="text-gray-700">${t.desc || ''}</p>
        <div class="relative bg-tempo-900 rounded-lg p-4 text-sm text-gray-300 mt-4 shadow-md border-l-4 border-l-tempo-gold">
            <pre class="code-block font-mono leading-relaxed text-gray-300" style="background: transparent; padding: 0; border: none; box-shadow: none; margin: 0;">${t.content}</pre>
        </div>`;
    } else {
        contentHtml = `
        <div class="highlight-box">
            <p>${t.content}</p>
        </div>`;
    }

    generatedHtml += `
        <!-- Slide ${slideNumber} -->
        <section id="topic-${slideNumber}" class="min-h-[85vh] flex flex-col justify-center mb-0 scroll-mt-10 border-b border-gray-200 py-10">
            <h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>${t.icon} ${t.title}</h3>
            <div class="prose max-w-none text-gray-700">
                ${contentHtml}
            </div>
        </section>
`;
});

// Sidebar links
let sidebarLinks = '';
additionalTopics.forEach((t, idx) => {
    const slideNumber = idx + 1;
    sidebarLinks += `
        <a href="#topic-${slideNumber}" class="nav-link flex items-center justify-between px-5 py-2.5 text-sm text-gray-300 transition-all border-l-[3px] border-transparent">
            <span class="pr-2 truncate">სექცია ${slideNumber}: ${t.title.replace(/<[^>]*>?/gm, '').trim().substring(0, 30)}...</span>
        </a>`;
});

let finalHtml = template;
finalHtml = finalHtml.replace(/{SESSION_NUMBER}/g, '4');
finalHtml = finalHtml.replace('{SESSION_TITLE}', 'სოც. მედია & ვიზუალი');
finalHtml = finalHtml.replace('{SESSION_TITLE}', 'სოციალური მედიის სტრატეგია <br><span class="text-tempo-light">+ AI მულტიმედია</span>');
finalHtml = finalHtml.replace('{SESSION_DESCRIPTION}', '30-დღიანი კონტენტ-კალენდარი, პოსტების ტექსტები (PAS/AIDA), და ვიზუალური/ვიდეო-მონახაზები AI-ით (Midjourney, ElevenLabs).');
finalHtml = finalHtml.replace(/{DURATION_MINUTES}/g, '180');
finalHtml = finalHtml.replace('{LECTURER_NAME}', 'გიორგი ბასილაია');
finalHtml = finalHtml.replace('{TOTAL_SECTIONS}', additionalTopics.length.toString());
finalHtml = finalHtml.replace('{SIDEBAR_LINKS}', sidebarLinks);
finalHtml = finalHtml.replace('{CONTENT_SECTIONS}', generatedHtml);

const chartScript = `
    const savCtx4 = document.getElementById('contentSavingsChart');
    if (savCtx4) {
        new Chart(savCtx4, {
            type: 'bar',
            data: {
                labels: ['ტრადიციული (~16 სთ)', 'AI (Claude+Midjourney)'],
                datasets: [{
                    label: 'დრო (საათები)',
                    data: [16, 1],
                    backgroundColor: ['#ef4444', '#C5A059'],
                    borderRadius: 4
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                plugins: { legend: { display: false } },
                scales: {
                    x: { ticks: { color: '#555' }, grid: { color: '#eee' } },
                    y: { ticks: { color: '#333', font: { size: 12, weight: 'bold' } }, grid: { display: false } }
                }
            }
        });
    }
</script>
</body>`;
finalHtml = finalHtml.replace('</script>\n</body>', chartScript);

fs.writeFileSync(pathSlides, finalHtml);
console.log("Lecture 4 MASSIVE generated successfully with " + additionalTopics.length + " slides.");
