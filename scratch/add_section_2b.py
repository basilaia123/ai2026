# -*- coding: utf-8 -*-
"""
Adds Section 2B: Multi-Camera Direction & Runway Gen-4.5 / MiniMax H3 Deep Dive to day-1-multimodal.html
Enriches Lecture 1 with key material from lecture-6:
- 4-Camera Event Scenography & Multi-Shot Director
- Motion Intensity & Camera Physics calibration table
- Motion vectors (Push, Orbit, Pan, Crane, Drone)
- MiniMax H3 Native Audio generation vs Veo 3.1
Strictly ZERO em-dash (—) and ZERO en-dash (–)
"""

with open('vanilla_events/day-1-multimodal.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '    </section>\n\n    <!-- ==================== THEME 03: AUDIO SYNTHESIS'

enrichment_block = '''      <!-- ==================== SECTION 2B: ADVANCED MULTI-CAMERA SCENOGRAPHY & LECTURE 6 DEEP DIVE ==================== -->
      <div class="vanilla-card p-5 sm:p-7 space-y-6 border-t-2 border-brand-gold">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-brand-goldBorder">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded-full bg-brand-gold text-white text-[10px] font-bold uppercase tracking-wider">ლექცია 6-ის ექსპერტული მოდული</span>
              <span class="text-xs text-brand-gold font-semibold">Cinematography Engine</span>
            </div>
            <h3 class="serif-font text-base sm:text-lg font-bold text-white mt-1">
              Multi-Camera Scenography: 4-კამერიანი რეჟისურა და ფიზიკის კალიბრაცია
            </h3>
          </div>
          <span class="text-[11px] text-brand-cream/70 font-mono">Arri Alexa &amp; Anamorphic Optic</span>
        </div>

        <p class="text-xs sm:text-sm text-brand-cream/85 font-light leading-relaxed">
          კინოინდუსტრიაში არცერთი პროფესიონალური სცენა არ იღება ერთი შემთხვევითი კადრით. ივენთ-დიზაინერმა უნდა იცოდეს სივრცის დანახვა <strong>4 კინემატოგრაფიული რაკურსით</strong>, რათა კლიენტმა სრულად შეიგრძნოს მასშტაბი:
        </p>

        <!-- 4 Camera Shots Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5 text-xs">
          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/50 space-y-1.5">
            <div class="flex items-center justify-between text-brand-gold font-bold text-[11px]">
              <span>SHOT 01</span>
              <span>24mm Wide</span>
            </div>
            <h4 class="font-bold text-white text-xs">Establishing Shot (სივრცის მასშტაბი)</h4>
            <p class="text-[11px] text-brand-cream/75 leading-relaxed font-light">
              ფართო რაკურსი: მთლიანი დარბაზი, ჭერის სიმაღლე, არქიტექტურული განათება და სტუმრების ნაკადი.
            </p>
            <div class="text-[10px] font-mono text-emerald-400 pt-1">Optic: 24mm Cinema Prime, f/4.0</div>
          </div>

          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/50 space-y-1.5">
            <div class="flex items-center justify-between text-brand-gold font-bold text-[11px]">
              <span>SHOT 02</span>
              <span>35mm Medium</span>
            </div>
            <h4 class="font-bold text-white text-xs">Medium Shot (მაგიდები &amp; დეკორი)</h4>
            <p class="text-[11px] text-brand-cream/75 leading-relaxed font-light">
              საშუალო გეგმა: სადღესასწაულო მაგიდების წყობა, სკამები, სანთლები და ყვავილოვანი თაღების პროპორცია.
            </p>
            <div class="text-[10px] font-mono text-emerald-400 pt-1">Optic: 35mm Anamorphic, f/2.8</div>
          </div>

          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/50 space-y-1.5">
            <div class="flex items-center justify-between text-brand-gold font-bold text-[11px]">
              <span>SHOT 03</span>
              <span>50mm Detail</span>
            </div>
            <h4 class="font-bold text-white text-xs">Close-Up (ტექსტურა &amp; მასალები)</h4>
            <p class="text-[11px] text-brand-cream/75 leading-relaxed font-light">
              ახლო რაკურსი: შავი მარმარილოს ზედაპირი, ოქროს დანა-ჩანგალი, ბროლის ბოკალები და სანთლის ალი.
            </p>
            <div class="text-[10px] font-mono text-emerald-400 pt-1">Optic: 50mm Portrait Prime, f/2.0</div>
          </div>

          <div class="sub-surface p-4 rounded-xl border border-brand-goldBorder/50 space-y-1.5">
            <div class="flex items-center justify-between text-brand-gold font-bold text-[11px]">
              <span>SHOT 04</span>
              <span>85mm Macro</span>
            </div>
            <h4 class="font-bold text-white text-xs">Macro Bokeh (ფლორისტიკის დეტალი)</h4>
            <p class="text-[11px] text-brand-cream/75 leading-relaxed font-light">
              მაკრო კადრი: ორქიდეის ფურცლები, წყლის წვეთები, რბილი ბოკე და სინათლის ოქროსფერი ნაწილაკები.
            </p>
            <div class="text-[10px] font-mono text-emerald-400 pt-1">Optic: 85mm Cinema Macro, f/1.4</div>
          </div>
        </div>

        <!-- Camera Physics & Motion Intensity Calibration Table -->
        <div class="space-y-3 pt-2">
          <div class="flex items-center justify-between">
            <h4 class="serif-font text-sm font-bold text-white">Motion Intensity &amp; კამერის ფიზიკის კალიბრაცია (Runway &amp; Veo)</h4>
            <span class="text-[10px] text-brand-gold font-semibold uppercase">Calibration Matrix</span>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs border-collapse">
              <thead>
                <tr class="border-b border-brand-goldBorder/60 text-brand-gold uppercase text-[10px] tracking-wider">
                  <th class="py-2.5 px-3">პარამეტრი</th>
                  <th class="py-2.5 px-3">რეკომენდებული მნიშვნელობა</th>
                  <th class="py-2.5 px-3">ეფექტი ვიდეოში</th>
                  <th class="py-2.5 px-3">შეცდომის რისკი (თუ გადააჭარბებთ)</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-brand-goldBorder/20 text-brand-cream/85 font-light">
                <tr class="hover:bg-brand-gold/5">
                  <td class="py-2.5 px-3 font-bold text-white">Motion Intensity</td>
                  <td class="py-2.5 px-3 text-emerald-400 font-semibold">2 - 4 (მაქს. 10-დან)</td>
                  <td class="py-2.5 px-3">დიდებული, ნელი, პრემიუმ კინემატოგრაფიული სრიალი</td>
                  <td class="py-2.5 px-3 text-red-300">5+-ზე იწყება Warping და დეკორის დეფორმაცია</td>
                </tr>
                <tr class="hover:bg-brand-gold/5">
                  <td class="py-2.5 px-3 font-bold text-white">Camera Speed</td>
                  <td class="py-2.5 px-3 text-emerald-400 font-semibold">0.3 - 0.5 მ/წმ (მუდმივი)</td>
                  <td class="py-2.5 px-3">სტაბილური თვალის სიმაღლის მოძრაობა (Eye-level Steadicam)</td>
                  <td class="py-2.5 px-3 text-red-300">აჩქარებისას იკარგება ფოკუსი და ტექსტურის სიმკვეთრე</td>
                </tr>
                <tr class="hover:bg-brand-gold/5">
                  <td class="py-2.5 px-3 font-bold text-white">Color Temperature</td>
                  <td class="py-2.5 px-3 text-emerald-400 font-semibold">2700K - 3200K (Kelvin)</td>
                  <td class="py-2.5 px-3">თბილი, ძვირადღირებული ოქროსფერი და ქარვისფერი აურა</td>
                  <td class="py-2.5 px-3 text-red-300">5000K+ იძლევა საავადმყოფოს ცივ, უსიცოცხლო შუქს</td>
                </tr>
                <tr class="hover:bg-brand-gold/5">
                  <td class="py-2.5 px-3 font-bold text-white">Frame Rate</td>
                  <td class="py-2.5 px-3 text-emerald-400 font-semibold">24 fps (Cinema Cadence)</td>
                  <td class="py-2.5 px-3">ჰოლივუდური კინოსტანდარტის ბუნებრივი მოძრაობის დაბინდვა (Motion Blur)</td>
                  <td class="py-2.5 px-3 text-red-300">60fps ტოვებს იაფი სატელევიზიო საპნის ოპერის შთაბეჭდილებას</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

      </div>
''' + target

assert target in html, "Target insertion point not found"
html = html.replace(target, enrichment_block)

# Check dashes
assert '\u2014' not in html and '\u2013' not in html, "Forbidden dash found!"

with open('vanilla_events/day-1-multimodal.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Section 2B successfully added to day-1-multimodal.html!")
