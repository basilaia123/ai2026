# -*- coding: utf-8 -*-
"""
Adds Comprehensive Step-by-Step Practical Guides (გაიდები) to day-1-multimodal.html:
- Guide 1: Custom AI Assistant setup walkthrough (Gemini Gem & Claude Project)
- Guide 2: Google Flow / Veo 3.1 & Runway Gen-4.5 I2V Production walkthrough
- Guide 3: Suno v6 Studio Music walkthrough
- Guide 4: ElevenLabs v3 Voiceover walkthrough
- Guide 5: Final Multi-Track Assembly walkthrough (CapCut / Premiere / DaVinci Resolve)
Strictly ZERO em-dash (—) and ZERO en-dash (–)
"""

with open('vanilla_events/day-1-multimodal.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Guide 1 in Theme 1 (before Task 1)
guide_1_target = '      </div>\n\n    </section>\n\n    <!-- ==================== TASK 1 (10 MINS) ==================== -->'

guide_1_content = '''      </div>

      <!-- ==================== PRACTICAL GUIDE 01: CUSTOM AI ASSISTANT SETUP ==================== -->
      <div class="vanilla-card p-5 sm:p-7 space-y-4 border-l-4 border-brand-gold">
        <div class="flex items-center justify-between pb-3 border-b border-brand-goldBorder">
          <div class="flex items-center gap-2">
            <span class="px-2.5 py-0.5 rounded-full bg-brand-gold text-white text-[10px] font-bold uppercase tracking-wider">პრაქტიკული გაიდი 01</span>
            <h3 class="serif-font text-base sm:text-lg font-bold text-white">
              ნაბიჯ-ნაბიჯ ინსტრუქცია: Custom AI რეჟისორის აწყობა Gemini Gem-სა და Claude-ში
            </h3>
          </div>
          <span class="text-xs text-brand-gold font-semibold uppercase hidden sm:inline">Playbook • Click-by-Click</span>
        </div>

        <p class="text-xs sm:text-sm text-brand-cream/85 font-light leading-relaxed">
          მიჰყევით ამ 6-საფეხურიან გაიდს, რათა თქვენი ასისტენტი მუდმივად მზად იყოს ივენთ-ბრიფების დასამუშავებლად:
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3.5 text-xs">
          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/40 space-y-2">
            <div class="flex items-center gap-2 text-brand-gold font-bold">
              <span class="w-5 h-5 rounded-full bg-brand-gold text-slate-950 flex items-center justify-center text-[10px]">1</span>
              <span>შესვლა და Gem-ის შექმნა</span>
            </div>
            <p class="text-[11px] text-brand-cream/80 leading-relaxed font-light">
              გადადით <strong>gemini.google.com/gems</strong> (ან <strong>claude.ai/projects</strong>). დააჭირეთ ღილაკს <strong>New Gem</strong> (ან Create Project).
            </p>
          </div>

          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/40 space-y-2">
            <div class="flex items-center gap-2 text-brand-gold font-bold">
              <span class="w-5 h-5 rounded-full bg-brand-gold text-slate-950 flex items-center justify-center text-[10px]">2</span>
              <span>სახელი და იდენტობა</span>
            </div>
            <p class="text-[11px] text-brand-cream/80 leading-relaxed font-light">
              სახელწოდებაში ჩაწერეთ: <code>Vanilla Events • AI Creative Director</code>. აღწერაში მიუთითეთ: <em>Luxury Event Scenographer &amp; Multimodal Director</em>.
            </p>
          </div>

          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/40 space-y-2">
            <div class="flex items-center gap-2 text-brand-gold font-bold">
              <span class="w-5 h-5 rounded-full bg-brand-gold text-slate-950 flex items-center justify-center text-[10px]">3</span>
              <span>სისტემური პრომპტის ჩასმა</span>
            </div>
            <p class="text-[11px] text-brand-cream/80 leading-relaxed font-light">
              ველში <strong>Instructions</strong> (ან System Prompt) ჩასვით ზემოთ მოცემული <strong>Master System Prompt</strong>. არ შეამოკლოთ, რათა ესთეტიკური კოდი შენარჩუნდეს.
            </p>
          </div>

          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/40 space-y-2">
            <div class="flex items-center gap-2 text-brand-gold font-bold">
              <span class="w-5 h-5 rounded-full bg-brand-gold text-slate-950 flex items-center justify-center text-[10px]">4</span>
              <span>ცოდნის ბაზის (Knowledge) მიბმა</span>
            </div>
            <p class="text-[11px] text-brand-cream/80 leading-relaxed font-light">
              ატვირთეთ Vanilla Events-ის მასალები (ფერთა პალიტრა, წარსული ივენთების ფოტოების აღწერები, რჩეული ლოკაციების სია: წინანდალი, შატო მუხრანი, რესპუბლიკა).
            </p>
          </div>

          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/40 space-y-2">
            <div class="flex items-center gap-2 text-brand-gold font-bold">
              <span class="w-5 h-5 rounded-full bg-brand-gold text-slate-950 flex items-center justify-center text-[10px]">5</span>
              <span>სატესტო ბრიფის გატესტვა</span>
            </div>
            <p class="text-[11px] text-brand-cream/80 leading-relaxed font-light">
              მიაწოდეთ ასისტენტს 3-ხაზიანი ბრიფი (ივენთის ტიპი, სტუმრები, განწყობა). დარწმუნდით, რომ პასუხში იძლევა 4-ვე ბლოკს (Storyboard, Flow, Suno, ElevenLabs).
            </p>
          </div>

          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/40 space-y-2">
            <div class="flex items-center gap-2 text-brand-gold font-bold">
              <span class="w-5 h-5 rounded-full bg-brand-gold text-slate-950 flex items-center justify-center text-[10px]">6</span>
              <span>Pin-ირება და გუნდური წვდომა</span>
            </div>
            <p class="text-[11px] text-brand-cream/80 leading-relaxed font-light">
              დააჭირეთ <strong>Save</strong> და მიამაგრეთ (Pin) Gem-ი მარცხენა მენიუში სწრაფი წვდომისთვის. საჭიროებისას გაუზიარეთ ბმული დიზაინერთა მთელ გუნდს.
            </p>
          </div>
        </div>
      </div>

    </section>

    <!-- ==================== TASK 1 (10 MINS) ==================== -->'''

if 'პრაქტიკული გაიდი 01' not in html:
    assert guide_1_target in html, "guide_1_target not found"
    html = html.replace(guide_1_target, guide_1_content)
    print("Guide 1 inserted.")
else:
    print("Guide 1 already present.")

# 2. Guide 2 in Theme 2 (Google Flow)
guide_2_target = '          </div>\n        </div>\n\n      </div>\n    </section>\n\n    <!-- ==================== THEME 03: AUDIO SYNTHESIS'

guide_2_content = '''          </div>
        </div>

      </div>

      <!-- ==================== PRACTICAL GUIDE 02: GOOGLE FLOW & VEO 3.1 I2V WORKFLOW ==================== -->
      <div class="vanilla-card p-5 sm:p-7 space-y-4 border-l-4 border-brand-gold">
        <div class="flex items-center justify-between pb-3 border-b border-brand-goldBorder">
          <div class="flex items-center gap-2">
            <span class="px-2.5 py-0.5 rounded-full bg-brand-gold text-white text-[10px] font-bold uppercase tracking-wider">პრაქტიკული გაიდი 02</span>
            <h3 class="serif-font text-base sm:text-lg font-bold text-white">
              ნაბიჯ-ნაბიჯ ინსტრუქცია: სტატიკური ესკიზიდან 4K კინემატოგრაფიულ ვიდეომდე (Google Flow Playbook)
            </h3>
          </div>
          <span class="text-xs text-brand-gold font-semibold uppercase hidden sm:inline">Production Workflow</span>
        </div>

        <p class="text-xs sm:text-sm text-brand-cream/85 font-light leading-relaxed">
          როგორ გადავაქციოთ დიზაინერის სტატიკური 3D რენდერი ან ფოტო ცოცხალ კინოკადრად Google Flow-სა და Veo 3.1-ში:
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-3.5 text-xs">
          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/40 space-y-2">
            <span class="text-[10px] font-bold text-brand-gold uppercase block">საფეხური 01</span>
            <h4 class="font-bold text-white text-xs">ფოტოს მომზადება (Asset Prep)</h4>
            <p class="text-[11px] text-brand-cream/80 leading-relaxed font-light">
              შეარჩიეთ მკაფიო, დაულაქავებელი ესკიზი. მოაცილეთ ტექსტური ლოგოები და watermark. შეინარჩუნეთ 16:9 (ეკრანისთვის) ან 9:16 (მობილურისთვის).
            </p>
          </div>

          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/40 space-y-2">
            <span class="text-[10px] font-bold text-brand-gold uppercase block">საფეხური 02</span>
            <h4 class="font-bold text-white text-xs">კამერის პრომპტის ჩასმა</h4>
            <p class="text-[11px] text-brand-cream/80 leading-relaxed font-light">
              ჩასვით AI ასისტენტის მიერ დაგენერირებული ოპტიკური პრომპტი (კამერის ვექტორი: <em>Slow Push-in</em> ან <em>Orbit 45</em>; ლინზა: <em>35mm</em>).
            </p>
          </div>

          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/40 space-y-2">
            <span class="text-[10px] font-bold text-brand-gold uppercase block">საფეხური 03</span>
            <h4 class="font-bold text-white text-xs">Motion Damping (Warping-ის პრევენცია)</h4>
            <p class="text-[11px] text-brand-cream/80 leading-relaxed font-light">
              Motion Intensity დააყენეთ <strong>2 - 3 / 10</strong>-ზე. ჩაამატეთ დირექტივა: <code>locked perspective, zero warping, stable geometry</code>.
            </p>
          </div>

          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/40 space-y-2">
            <span class="text-[10px] font-bold text-brand-gold uppercase block">საფეხური 04</span>
            <h4 class="font-bold text-white text-xs">გენერაცია &amp; 4K ექსპორტი</h4>
            <p class="text-[11px] text-brand-cream/80 leading-relaxed font-light">
              დააჭირეთ Generate. შეაფასეთ სანთლების ალისა და ნისლის ბუნებრიობა. დააჭირეთ <strong>Upscale to 4K</strong> და გადმოწერეთ MP4 ფაილი.
            </p>
          </div>
        </div>
      </div>

    </section>

    <!-- ==================== THEME 03: AUDIO SYNTHESIS'''

assert guide_2_target in html, "guide_2_target not found"
html = html.replace(guide_2_target, guide_2_content)
print("Guide 2 inserted.")

# 3. Guide 3, 4, 5 in Theme 3 / Audio (before Task 2)
guide_345_target = '        </div>\n\n      </div>\n    </section>\n\n    <!-- ==================== TASK 2 (10 MINS) ==================== -->'

guide_345_content = '''        </div>

      </div>

      <!-- ==================== PRACTICAL GUIDES 03 & 04: AUDIO & VOICEOVER ENGINEERING ==================== -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        
        <!-- Guide 03: Suno v6 Playbook -->
        <div class="vanilla-card p-5 space-y-3 border-l-4 border-brand-gold">
          <div class="flex items-center justify-between pb-2 border-b border-brand-goldBorder">
            <span class="px-2 py-0.5 rounded-full bg-brand-gold text-white text-[10px] font-bold uppercase">პრაქტიკული გაიდი 03</span>
            <span class="text-xs font-mono text-brand-gold">Suno v6 Playbook</span>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">Suno v6-ში ივენთის საუნდტრეკის შექმნის წესები</h4>
          <ol class="text-xs text-brand-cream/80 space-y-2 font-light list-decimal list-inside leading-relaxed">
            <li><strong>Custom Mode &amp; Instrumental:</strong> ყოველთვის ჩართეთ <em>Custom Mode</em> და მონიშნეთ <em>Instrumental</em>, რათა თავიდან აიცილოთ არასასურველი ვოკალი;</li>
            <li><strong>სტილის ფორმულა:</strong> ჩასვით: <code>[Style: Luxury Gala Lounge, 102 BPM, warm Rhodes piano, gentle cello pads, atmospheric, instrumental only]</code>;</li>
            <li><strong>სტრუქტურული თეგები:</strong> Lyrics ველში ჩასვით მხოლოდ სტრუქტურის მარკერები: <code>[Intro] [Ambient Theme] [Subtle Build] [Outro Fade]</code>;</li>
            <li><strong>Stems ექსპორტი:</strong> მოწონებული ტრეკისთვის გამოიყენეთ <em>Create Stems</em>, რათა ცალკე მიიღოთ მელოდია და ბასი ვიდეო მონტაჟისთვის.</li>
          </ol>
        </div>

        <!-- Guide 04: ElevenLabs v3 Playbook -->
        <div class="vanilla-card p-5 space-y-3 border-l-4 border-brand-gold">
          <div class="flex items-center justify-between pb-2 border-b border-brand-goldBorder">
            <span class="px-2 py-0.5 rounded-full bg-brand-gold text-white text-[10px] font-bold uppercase">პრაქტიკული გაიდი 04</span>
            <span class="text-xs font-mono text-brand-gold">ElevenLabs Playbook</span>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">ElevenLabs v3-ში პრესტიჟული ხმის გაჟღერების წესები</h4>
          <ol class="text-xs text-brand-cream/80 space-y-2 font-light list-decimal list-inside leading-relaxed">
            <li><strong>Voice Selection:</strong> შეარჩიეთ ღრმა, ხავერდოვანი ტემბრი (Voice Library -> Luxury / Narrative);</li>
            <li><strong>პაუზების სინტაქსი:</strong> გამოიყენეთ მრავალწერტილი (<code>...</code>) ყოველი წინადადების შემდეგ 0.5-წამიანი საზეიმო პაუზისთვის;</li>
            <li><strong>Voice Settings:</strong> Stability დააყენეთ <strong>70%</strong>-ზე (სტაბილური ელიტური ტონი), Clarity <strong>80%</strong>-ზე, Style Exaggeration <strong>15%</strong>-ზე;</li>
            <li><strong>ორენოვანი ექსპორტი:</strong> დააგენერირეთ როგორც ქართული, ისე ინგლისური ვერსია და შეინახეთ WAV / MP3 44.1kHz ფორმატში.</li>
          </ol>
        </div>

      </div>

      <!-- ==================== PRACTICAL GUIDE 05: MULTI-TRACK ASSEMBLY & MASTERING ==================== -->
      <div class="vanilla-card p-5 sm:p-7 space-y-4 border-l-4 border-emerald-500 bg-emerald-950/10">
        <div class="flex items-center justify-between pb-3 border-b border-emerald-500/30">
          <div class="flex items-center gap-2">
            <span class="px-2.5 py-0.5 rounded-full bg-emerald-500 text-slate-950 text-[10px] font-bold uppercase tracking-wider">პრაქტიკული გაიდი 05</span>
            <h3 class="serif-font text-base sm:text-lg font-bold text-white">
              მულტიმოდალური პაკეტის გაერთიანება &amp; მონტაჟი (CapCut / Premiere / DaVinci Resolve)
            </h3>
          </div>
          <span class="text-xs text-emerald-400 font-semibold uppercase hidden sm:inline">Final Polish</span>
        </div>

        <p class="text-xs sm:text-sm text-brand-cream/85 font-light leading-relaxed">
          საბოლოო ეტაპზე დიზაინერი აერთიანებს 3 ელემენტს: Veo-ს ვიდეოს, Suno-ს საუნდტრეკსა და ElevenLabs-ის ხმას:
        </p>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-3.5 text-xs">
          <div class="sub-surface p-4 rounded-xl border border-emerald-500/30 space-y-1.5">
            <span class="font-bold text-emerald-400 block text-xs">1. აუდიო დაკინგი (-18dB წესი)</span>
            <p class="text-[11px] text-brand-cream/80 leading-relaxed font-light">
              სანამ სპიკერი საუბრობს, ფონური მუსიკა ავტომატურად დაიყვანეთ <strong>-18dB</strong>-ზე. როდესაც სპიკერი ჩუმდება, მუსიკა ამოდის <strong>-6dB</strong>-მდე.
            </p>
          </div>

          <div class="sub-surface p-4 rounded-xl border border-emerald-500/30 space-y-1.5">
            <span class="font-bold text-emerald-400 block text-xs">2. ფერთა კორექცია (Color Grading)</span>
            <p class="text-[11px] text-brand-cream/80 leading-relaxed font-light">
              დაამატეთ მსუბუქი თბილი LUT (Gold &amp; Emerald), რათა ვიდეოს ფერები იდეალურად დაემთხვეს Vanilla Events-ის ოქროსფერ და ზურმუხტისფერ დიზაინ-კოდს.
            </p>
          </div>

          <div class="sub-surface p-4 rounded-xl border border-emerald-500/30 space-y-1.5">
            <span class="font-bold text-emerald-400 block text-xs">3. ფორმატები და ჩაბარება</span>
            <p class="text-[11px] text-brand-cream/80 leading-relaxed font-light">
              დააექსპორტეთ 2 ვერსია: <strong>16:9 4K</strong> (დიდი LED ეკრანებისა და ვებ პორტალისთვის) და <strong>9:16 Full HD</strong> (მობილური ციფრული მოსაწვევებისთვის).
            </p>
          </div>
        </div>
      </div>

    </section>

    <!-- ==================== TASK 2 (10 MINS) ==================== -->'''

assert guide_345_target in html, "guide_345_target not found"
html = html.replace(guide_345_target, guide_345_content)
print("Guides 3, 4, 5 inserted.")

# Dash check
assert '\u2014' not in html and '\u2013' not in html, "Dash found!"

with open('vanilla_events/day-1-multimodal.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("All 5 Guides successfully integrated into day-1-multimodal.html!")
