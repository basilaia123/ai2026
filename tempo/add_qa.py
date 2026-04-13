with open('lecture-6-slides.html', 'r', encoding='utf-8') as f:
    content = f.read()

qa_block = """
            <!-- Structured Q&A closing panel -->
            <div class="mt-6 bg-white border border-gray-200 rounded-xl overflow-hidden shadow-sm">
                <div class="bg-tempo-900 px-5 py-3 flex items-center justify-between">
                    <h4 class="text-tempo-gold font-bold text-sm">&#10067; სტრუქტურირებული Q&#38;A &#8212; კურსის დასასრული <span class="text-gray-400 font-normal">(10&#8211;13 წთ)</span></h4>
                    <span class="bg-tempo-gold/20 text-tempo-gold text-xs font-bold px-3 py-1 rounded border border-tempo-gold/30">ინსტრუქტორი ემზადება წინასწარ</span>
                </div>
                <div class="p-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <h5 class="font-bold text-tempo-900 text-sm mb-3">&#128293; ყველაზე ხშირი კითხვები:</h5>
                            <div class="space-y-3">
                                <div class="border border-gray-100 rounded-lg p-3 bg-gray-50">
                                    <p class="text-xs font-bold text-tempo-900 mb-1">"AI შეცვლის ჩვენს სამუშაოს?"</p>
                                    <p class="text-xs text-gray-600">&#8594; AI ცვლის <em>ამოცანებს</em>, არა ადამიანებს. ვინც AI-ს იყენებს &#8212; ადგილს ინარჩუნებს. ვინც &#8212; არა, მის ადგილს AI-ის მომხმარებელი იკავებს.</p>
                                </div>
                                <div class="border border-gray-100 rounded-lg p-3 bg-gray-50">
                                    <p class="text-xs font-bold text-tempo-900 mb-1">"რომელი ინსტრუმენტით დავიწყო?"</p>
                                    <p class="text-xs text-gray-600">&#8594; Claude.ai &#8212; ქართული, ხვალვე 15 წთ. Make.com &#8212; IT-სთან ერთად 2 კვ-ში.</p>
                                </div>
                                <div class="border border-gray-100 rounded-lg p-3 bg-gray-50">
                                    <p class="text-xs font-bold text-tempo-900 mb-1">"AI-ს Output-ს ყოველთვის ვამოწმებ?"</p>
                                    <p class="text-xs text-gray-600">&#8594; კლიენტთან გაგზავნამდე &#8212; ყოველთვის. შიდა სამუშაოსთვის &#8212; პირველ 2 კვ-ში, შემდეგ ნდობა იზრდება.</p>
                                </div>
                                <div class="border border-gray-100 rounded-lg p-3 bg-gray-50">
                                    <p class="text-xs font-bold text-tempo-900 mb-1">"როდის დავინახავ რეალურ ეფექტს?"</p>
                                    <p class="text-xs text-gray-600">&#8594; 1-ლ კვ-ში &#8212; Follow-up-ის დროის შემცირება. 1 თვეში &#8212; 15%+ ეფ. ზრდა. 3 თვეში &#8212; სისტემური შედეგი.</p>
                                </div>
                            </div>
                        </div>
                        <div>
                            <h5 class="font-bold text-tempo-900 text-sm mb-3">&#128203; ვალდებულება &#8212; სესიის დასასრულს:</h5>
                            <p class="text-xs text-gray-600 mb-3">ყველა მონაწილე Google Meet Chat-ში წერს <strong>1 კონკრეტულ ვალდებულებას</strong> &#8212; რას გააკეთებ <strong>ხვალ, სამუშაო დღეს:</strong></p>
                            <div class="bg-tempo-900 rounded-lg p-4 text-xs text-gray-300 space-y-2 mb-3">
                                <div class="flex items-start gap-2"><span class="text-green-400">&#10003;</span> "ხვალ Claude Project-ს შევქმნი და Sales Script-ს ჩავდებ"</div>
                                <div class="flex items-start gap-2"><span class="text-green-400">&#10003;</span> "NotebookLM-ი 2 ხელშეკრულებით კვირაში ჩამოვტვირთავ"</div>
                                <div class="flex items-start gap-2"><span class="text-green-400">&#10003;</span> "IT-სთან შეხვედრა 72-სთ Reminder Scenario-ზე"</div>
                                <div class="flex items-start gap-2 opacity-40"><span class="text-red-400">&#10007;</span> "ვეცდები AI-ს გამოვიყენო" &#8212; ძალიან ბუნდოვანია</div>
                            </div>
                            <div class="bg-tempo-gold/10 border border-tempo-gold/30 rounded p-3 text-xs text-gray-700">
                                <strong class="text-tempo-900">&#128161; 30 დღის შემდეგ:</strong> ინსტრუქტორი გუნდს ეკითხება &#8212; "რა გაკეთდა? რა შეჩერდა?" &#8212; ანგარიშვალდებულება ეფექტს 3-ჯერ ზრდის.
                            </div>
                        </div>
                    </div>
                </div>
            </div>"""

# Insert before the closing </section> of topic-12
marker = '        </section>\n\n    </div>\n'
idx = content.rfind(marker)  # last occurrence = topic-12 end
if idx != -1:
    content = content[:idx] + qa_block + '\n' + content[idx:]
    print(f'Q&A block inserted at {idx}')
else:
    marker2 = '        </section>\r\n\r\n    </div>\r\n'
    idx2 = content.rfind(marker2)
    if idx2 != -1:
        content = content[:idx2] + qa_block + '\r\n' + content[idx2:]
        print(f'Q&A block inserted (CRLF) at {idx2}')
    else:
        print('Marker not found')
        i = content.find('</div>\n</main>')
        print(repr(content[max(0,i-200):i+50]))

with open('lecture-6-slides.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done. File size:', len(content))
