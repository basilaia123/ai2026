with open('lecture-6-slides.html', 'r', encoding='utf-8') as f:
    content = f.read()

instructor_block = """
            <!-- Instructor live walkthrough -->
            <div class="bg-white border border-gray-200 rounded-xl overflow-hidden shadow-sm mt-6">
                <div class="bg-blue-900 px-5 py-3 flex items-center justify-between">
                    <h4 class="text-white font-bold text-sm">&#127916; ინსტრუქტორის ლაივ სკრიპტი &#8212; ეტაპობრივი დემო</h4>
                    <span class="bg-white/20 text-white text-xs font-bold px-3 py-1 rounded">&#128274; ინსტრუქტორისთვის</span>
                </div>
                <div class="p-6">
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-5">
                        <div class="border border-blue-200 rounded-lg p-4 bg-blue-50">
                            <div class="flex items-center gap-2 mb-3">
                                <span class="w-7 h-7 bg-blue-700 text-white rounded-full flex items-center justify-center text-xs font-bold shrink-0">1</span>
                                <span class="font-bold text-blue-900 text-sm">make.com-ის გახსნა <span class="font-normal text-xs text-blue-700">(3 წთ)</span></span>
                            </div>
                            <ul class="text-xs text-gray-700 space-y-1.5">
                                <li>&#8594; ბრაუზერი: <strong>make.com &#8594; My Scenarios</strong></li>
                                <li>&#8594; გახსნა: Scenario <em>Tempo Lead to WA</em></li>
                                <li>&#8594; Canvas: <strong>4 module ერთ ხაზზე</strong> - ვაჩვენოთ</li>
                                <li>&#8594; <em>"ეს ხდება ავტომატურად &#8212; ადამიანი არ ერთვება"</em></li>
                                <li>&#8594; Watch New Row-ის კავშირი Sheets-სთან</li>
                            </ul>
                        </div>
                        <div class="border border-purple-200 rounded-lg p-4 bg-purple-50">
                            <div class="flex items-center gap-2 mb-3">
                                <span class="w-7 h-7 bg-purple-700 text-white rounded-full flex items-center justify-center text-xs font-bold shrink-0">2</span>
                                <span class="font-bold text-purple-900 text-sm">HTTP module &#8212; Claude API <span class="font-normal text-xs text-purple-700">(5 წთ)</span></span>
                            </div>
                            <ul class="text-xs text-gray-700 space-y-1.5">
                                <li>&#8594; ორჯერ დაწკაპება &#8594; Request Body ჩანს</li>
                                <li>&#8594; ეკრანზე: {{1.name}}, {{1.budget}} ცვლადები</li>
                                <li>&#8594; <em>"Sheets-ის სტრიქონიდან ავტომატურად ივსება"</em></li>
                                <li>&#8594; API Key: * * * * * * (უსაფრთხოდ ინახება)</li>
                                <li>&#8594; Response mapping &#8594; WhatsApp message</li>
                            </ul>
                        </div>
                        <div class="border border-green-200 rounded-lg p-4 bg-green-50">
                            <div class="flex items-center gap-2 mb-3">
                                <span class="w-7 h-7 bg-green-700 text-white rounded-full flex items-center justify-center text-xs font-bold shrink-0">3</span>
                                <span class="font-bold text-green-900 text-sm">რეალური გაშვება <span class="font-normal text-xs text-green-700">(7 წთ)</span></span>
                            </div>
                            <ul class="text-xs text-gray-700 space-y-1.5">
                                <li>&#8594; Google Forms &#8594; <strong>ტესტ-ლიდი შევსება</strong></li>
                                <li>&#8594; <em>გიორგი მ., 2-ოთახი, ბიუჯეტი: $150k</em></li>
                                <li>&#8594; Make.com: <strong>Run once</strong> &#8594; ვუყურებთ live</li>
                                <li>&#8594; Claude Output &#8212; სრული ტექსტი ეკრანზე</li>
                                <li>&#8594; Sheets: სტრიქონი &#8212; "WA გაგზავნილია &#10003;"</li>
                                <li>&#8594; <strong>დებრიფი: "ადრე 5 წთ, ახლა &#8212; 18 წამი"</strong></li>
                            </ul>
                        </div>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="bg-amber-50 border border-amber-200 rounded-lg p-4">
                            <h5 class="font-bold text-amber-900 mb-3 text-sm">&#128172; მოსალოდნელი კითხვები:</h5>
                            <ul class="text-xs text-gray-700 space-y-2">
                                <li><strong>"WhatsApp API კომპლიცირებულია?"</strong><br>&#8594; Twilio sandbox &#8212; ტესტისთვის. ბიზნეს-ვერიფ. IT-ს ამოცანაა.</li>
                                <li><strong>"Claude-ის API ძვირი?"</strong><br>&#8594; 200 ლიდი/თვე &#8776; $0.40. ფაქტობრივად უფასოა.</li>
                                <li><strong>"ქართული ტექსტი გამოდის?"</strong><br>&#8594; კი &#8212; Claude პირდაპირ ქართულად. ვაჩვენოთ ეკრანზე.</li>
                                <li><strong>"CRM (Bitrix/HubSpot) ვიყენებთ?"</strong><br>&#8594; Make.com-ს 1500+ integration &#8212; ნებისმიერ CRM-ს უკავშირდება.</li>
                            </ul>
                        </div>
                        <div class="bg-tempo-900 rounded-lg p-4">
                            <h5 class="font-bold text-tempo-gold mb-3 text-sm">&#128279; Bonus: Scenario 2 &#8212; 72-სთ Follow-up Reminder</h5>
                            <ol class="text-xs text-gray-300 space-y-2">
                                <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold">1.</span> Sheets: "ბოლო კონტაქტი" სვეტი &#8212; თარიღი</li>
                                <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold">2.</span> Schedule trigger &#8212; ყოველდღე 10:00</li>
                                <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold">3.</span> Filter: +72სთ გავიდა AND სტ. &#8800; "დახურული"</li>
                                <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold">4.</span> Gmail &#8594; მენ: "&#9888; 3 დღე &#8212; დაურეკეთ"</li>
                                <li class="flex items-start gap-2 text-gray-400 italic"><span class="text-tempo-gold font-bold not-italic">&#8594;</span> გამართვა 20 წთ. ეფექტი: გაყიდვები +15%</li>
                            </ol>
                        </div>
                    </div>
                </div>
            </div>"""

# Find the end of topic-5b section and insert before it
marker = '        </section>\n\n        <!-- Slide 6: Security'
idx = content.find(marker)
if idx != -1:
    content = content[:idx] + instructor_block + '\n' + content[idx:]
    print(f'Inserted at position {idx}')
else:
    # Try with \r\n
    marker2 = '        </section>\r\n\r\n        <!-- Slide 6: Security'
    idx2 = content.find(marker2)
    if idx2 != -1:
        content = content[:idx2] + instructor_block + '\r\n' + content[idx2:]
        print(f'Inserted (CRLF) at position {idx2}')
    else:
        print('Marker not found! Searching nearby...')
        i = content.find('Slide 6: Security')
        print(f'Slide 6 found at: {i}, nearby: {repr(content[i-120:i+30])}')

with open('lecture-6-slides.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done. File size:', len(content))
