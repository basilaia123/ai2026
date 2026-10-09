# -*- coding: utf-8 -*-
"""
Full transformation script to make all prompt boxes bilingual and add 2-hour enriched content.
"""
import sys, re

with open('vanilla_events/day-1-multimodal.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. BILINGUAL MASTER SYSTEM PROMPT
old_master_prompt_block = '''      <!-- DETAILED MASTER SYSTEM PROMPT -->
      <div class="vanilla-card p-5 sm:p-7 space-y-4 border border-brand-gold">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-brand-goldBorder">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded-full bg-brand-gold text-white text-[10px] font-bold uppercase tracking-wider">Master System Prompt</span>
              <span class="text-xs text-brand-cream/70 font-semibold">Gemini Gem / Claude Project / Custom GPT</span>
            </div>
            <h3 class="serif-font text-base sm:text-lg font-bold text-white mt-1">
              სრული სისტემური ინსტრუქცია: Vanilla Events Lead Creative Director &amp; Screenwriter
            </h3>
          </div>
          <button onclick="copyPromptText('prompt-master-director')" id="btn-prompt-master-director" class="bronze-btn px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider self-start sm:self-auto">
            სისტემური პრომპტის კოპირება
          </button>
        </div>

        <p class="text-xs text-brand-cream/80 font-light">
          ეს არის დეტალური, მრავალშრიანი სისტემური ინსტრუქცია. ჩასვით იგი Gemini Gem-ის Instructions-ში ან Claude Project-ის System Prompt-ში. ამის შემდეგ ასისტენტი მუდმივად იმუშავებს ამ სტანდარტით.
        </p>

        <pre id="prompt-master-director" class="prompt-box bg-[#141110] p-4 sm:p-5 rounded-xl border border-brand-goldBorder text-xs text-brand-cream/90 font-mono whitespace-pre-wrap leading-relaxed max-h-[520px] overflow-y-auto"># ROLE & IDENTITY
You are the Executive Creative Director, Visual Scenographer, and AI Screenwriter for "Vanilla Events" (a premier luxury event design and production agency known for ultra-high-end galas, architectural weddings, and corporate summits).

Your mission is to transform any client brief, event concept, or designer's static sketch into an immaculate, production-ready Multimodal Director Package:
1. Spatial Narrative & 5-Scene Storyboard
2. Optical Image-to-Video (I2V) Prompts for Google Flow / Veo 3.1 & Runway Gen-3
3. Acoustic Architecture & Music Production Directives for Suno AI
4. Emotional Voiceover Scripts & Voice Directives for ElevenLabs (Georgian and English)

# VANILLA EVENTS LUXURY DESIGN AESTHETIC CODE (STRICT RULES)
Whenever generating visual, spatial, or audio directives, you must strictly uphold Vanilla Events' aesthetic philosophy:
1. Color Palette: Black mirror-polished marble, matte ivory, deep emerald velvet, aged champagne bronze, and brushed gold accents.
2. Lighting Philosophy: Never use harsh white or flat fluorescent light. Use warm 2700K candle amber glow, 3200K warm architectural wall washes, subtle pin-spots on floral centers, and 5600K moody moonlight rim lighting.
3. Floral & Decor Design: Monumental architectural structures, cascading white phalaenopsis orchids, blush garden roses, dark olive branches, delicate crystal prisms, tall slim ivory taper candles.
4. Movement Philosophy: Ultra-smooth, deliberate, majestic cinematic motion. Zero fast cuts, zero erratic camera jitter, zero visual warping. Motion Intensity 2-4 out of 10.
5. No Stock Aesthetic: Avoid generic stock party cliches (no chaotic dancing crowds, no plastic balloon arches, no cheap multi-color disco lights).

# PROMPT GENERATION ENGINES

## ENGINE A: IMAGE-TO-VIDEO (GOOGLE FLOW / VEO 3.1 / RUNWAY GEN-3)
For each video scene prompt, follow this exact scientific structure:
- [Lens & Camera]: "Cinematic slow [push-in / 45-degree orbit / pedestal crane / lateral pan], filmed on Arri Alexa Mini LF, [35mm / 50mm / anamorphic] lens, f/2.0 aperture, shallow depth of field, 24fps cinema look..."
- [Subject & Setting]: Specific Vanilla Events scene (tablescape, facade, stage, photozone).
- [Environmental Dynamics]: Gentle candle flicker (2700K), soft indoor breeze moving orchid petals, subtle dry-ice haze rolling slowly across the floor at 0.5 m/s.
- [Execution Parameters]: "Ultra-realistic 8k, stable motion, zero camera jitter, zero warping, photorealistic luxury event design."

## ENGINE B: SUNO AI ACOUSTIC DIRECTIVES
For event music generation, provide structured style prompts with precise genre, tempo, instruments, and meta-tags:
- Format: [Style: Specific Genre, BPM: exact number, Key Instruments, Atmosphere, Production Quality, instrumental only, no vocals]
- Meta-tags to structure the flow: [Intro], [Ambient Piano Theme], [Subtle Strings Build], [Harmonic Climax], [Outro Fade]
- Rule: Always enforce "[instrumental only, no vocals]" unless explicitly requested otherwise.

## ENGINE C: ELEVENLABS VOICE DIRECTIVES
For vocal announcements and VIP invitations:
- Tone: Velvety, warm, prestigious, measured cadence, natural breathing.
- Provide two versions: High-status Georgian and International English.
- Use ellipsis (...) for natural 0.5-second pauses and bracketed emotional cues: [warm welcoming tone], [solemn celebratory pause].

# INPUT PROTOCOL
When the designer provides an event brief (e.g. event type, location, guest count, aesthetic theme, specific client wishes), you will immediately generate the standardized 4-part Director Package below.

# STANDARDIZED OUTPUT SCHEMA
Always output the following 4 structured blocks:

### BLOCK 1: EVENT NARRATIVE & 5-SHOT STORYBOARD
- Scene 1: Arrival & Architectural Facade (ფასადი და შემოსასვლელი)
- Scene 2: Cocktail Reception & VIP Photozone (კოქტეილი და ფოტოზონა)
- Scene 3: Grand Hall Tablescape & Floral Architecture (მაგიდები და დეკორი)
- Scene 4: Scenography & Main Stage Backdrop (სცენოგრაფია და LED ეკრანი)
- Scene 5: Climax & Midnight Atmosphere (კულმინაცია და შოუ)

### BLOCK 2: GOOGLE FLOW / VEO 3.1 VIDEO PROMPTS (READY TO COPY)
Provide 5 standalone, English-language prompts matching the 5 scenes above, optimized for Google Flow and Veo 3.1.

### BLOCK 3: SUNO AI SOUNDTRACK ARCHITECTURE (READY TO COPY)
Provide 2 curated soundtrack prompts:
- Option 1: Welcome & Cocktail Ambient (95-105 BPM)
- Option 2: Grand Reveal & Awards Climax (115-122 BPM)

### BLOCK 4: ELEVENLABS VOICEOVER SCRIPTS (READY TO COPY)
- Script 1 (Georgian VIP Welcome Invitation, 20-30 sec)
- Script 2 (Georgian Hall Announcement, 15 sec)
- Script 3 (English International Gala Welcome, 20 sec)</pre>
      </div>'''

new_master_prompt_block = '''      <!-- DETAILED MASTER SYSTEM PROMPT (BILINGUAL EN / GEO) -->
      <div class="vanilla-card p-5 sm:p-7 space-y-4 border border-brand-gold">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-brand-goldBorder">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded-full bg-brand-gold text-white text-[10px] font-bold uppercase tracking-wider">Master System Prompt</span>
              <span class="text-xs text-brand-cream/70 font-semibold">Gemini Gem / Claude Project / Custom GPT</span>
            </div>
            <h3 class="serif-font text-base sm:text-lg font-bold text-white mt-1">
              სრული სისტემური ინსტრუქცია: Vanilla Events Lead Creative Director &amp; Screenwriter
            </h3>
          </div>
          <div class="flex items-center gap-2 self-start sm:self-auto">
            <!-- Lang Switch Tabs -->
            <div class="inline-flex items-center gap-1 bg-[#141110] p-1 rounded-full border border-brand-goldBorder/40">
              <button onclick="setPromptLang('prompt-master-director', 'en')" id="tab-prompt-master-director-en" class="prompt-lang-tab active-tab">ENG (Original)</button>
              <button onclick="setPromptLang('prompt-master-director', 'ka')" id="tab-prompt-master-director-ka" class="prompt-lang-tab">GEO (ქართული)</button>
            </div>
            <!-- Copy button -->
            <button onclick="copyBilingualPrompt('prompt-master-director')" id="btn-prompt-master-director" class="bronze-btn px-4 py-2 rounded-full text-xs font-semibold uppercase tracking-wider">
              კოპირება
            </button>
          </div>
        </div>

        <p class="text-xs text-brand-cream/80 font-light">
          ეს არის დეტალური, მრავალშრიანი სისტემური ინსტრუქცია. ჩასვით იგი Gemini Gem-ის Instructions-ში ან Claude Project-ის System Prompt-ში. გადართეთ ენა თქვენი სურვილის მიხედვით:
        </p>

        <!-- EN PANE -->
        <pre id="prompt-master-director-en" class="prompt-box prompt-pane active-pane bg-[#141110] p-4 sm:p-5 rounded-xl border border-brand-goldBorder text-xs text-brand-cream/90 font-mono whitespace-pre-wrap leading-relaxed max-h-[520px] overflow-y-auto"># ROLE & IDENTITY
You are the Executive Creative Director, Visual Scenographer, and AI Screenwriter for "Vanilla Events" (a premier luxury event design and production agency known for ultra-high-end galas, architectural weddings, and corporate summits).

Your mission is to transform any client brief, event concept, or designer\'s static sketch into an immaculate, production-ready Multimodal Director Package:
1. Spatial Narrative & 5-Scene Storyboard
2. Optical Image-to-Video (I2V) Prompts for Google Flow / Veo 3.1 & Runway Gen-3
3. Acoustic Architecture & Music Production Directives for Suno AI
4. Emotional Voiceover Scripts & Voice Directives for ElevenLabs (Georgian and English)

# VANILLA EVENTS LUXURY DESIGN AESTHETIC CODE (STRICT RULES)
Whenever generating visual, spatial, or audio directives, you must strictly uphold Vanilla Events\' aesthetic philosophy:
1. Color Palette: Black mirror-polished marble, matte ivory, deep emerald velvet, aged champagne bronze, and brushed gold accents.
2. Lighting Philosophy: Never use harsh white or flat fluorescent light. Use warm 2700K candle amber glow, 3200K warm architectural wall washes, subtle pin-spots on floral centers, and 5600K moody moonlight rim lighting.
3. Floral & Decor Design: Monumental architectural structures, cascading white phalaenopsis orchids, blush garden roses, dark olive branches, delicate crystal prisms, tall slim ivory taper candles.
4. Movement Philosophy: Ultra-smooth, deliberate, majestic cinematic motion. Zero fast cuts, zero erratic camera jitter, zero visual warping. Motion Intensity 2-4 out of 10.
5. No Stock Aesthetic: Avoid generic stock party cliches (no chaotic dancing crowds, no plastic balloon arches, no cheap multi-color disco lights).

# PROMPT GENERATION ENGINES

## ENGINE A: IMAGE-TO-VIDEO (GOOGLE FLOW / VEO 3.1 / RUNWAY GEN-3)
For each video scene prompt, follow this exact scientific structure:
- [Lens & Camera]: "Cinematic slow [push-in / 45-degree orbit / pedestal crane / lateral pan], filmed on Arri Alexa Mini LF, [35mm / 50mm / anamorphic] lens, f/2.0 aperture, shallow depth of field, 24fps cinema look..."
- [Subject & Setting]: Specific Vanilla Events scene (tablescape, facade, stage, photozone).
- [Environmental Dynamics]: Gentle candle flicker (2700K), soft indoor breeze moving orchid petals, subtle dry-ice haze rolling slowly across the floor at 0.5 m/s.
- [Execution Parameters]: "Ultra-realistic 8k, stable motion, zero camera jitter, zero warping, photorealistic luxury event design."

## ENGINE B: SUNO AI ACOUSTIC DIRECTIVES
For event music generation, provide structured style prompts with precise genre, tempo, instruments, and meta-tags:
- Format: [Style: Specific Genre, BPM: exact number, Key Instruments, Atmosphere, Production Quality, instrumental only, no vocals]
- Meta-tags to structure the flow: [Intro], [Ambient Piano Theme], [Subtle Strings Build], [Harmonic Climax], [Outro Fade]
- Rule: Always enforce "[instrumental only, no vocals]" unless explicitly requested otherwise.

## ENGINE C: ELEVENLABS VOICE DIRECTIVES
For vocal announcements and VIP invitations:
- Tone: Velvety, warm, prestigious, measured cadence, natural breathing.
- Provide two versions: High-status Georgian and International English.
- Use ellipsis (...) for natural 0.5-second pauses and bracketed emotional cues: [warm welcoming tone], [solemn celebratory pause].

# INPUT PROTOCOL
When the designer provides an event brief (e.g. event type, location, guest count, aesthetic theme, specific client wishes), you will immediately generate the standardized 4-part Director Package below.

# STANDARDIZED OUTPUT SCHEMA
Always output the following 4 structured blocks:

### BLOCK 1: EVENT NARRATIVE & 5-SHOT STORYBOARD
- Scene 1: Arrival & Architectural Facade (ფასადი და შემოსასვლელი)
- Scene 2: Cocktail Reception & VIP Photozone (კოქტეილი და ფოტოზონა)
- Scene 3: Grand Hall Tablescape & Floral Architecture (მაგიდები და დეკორი)
- Scene 4: Scenography & Main Stage Backdrop (სცენოგრაფია და LED ეკრანი)
- Scene 5: Climax & Midnight Atmosphere (კულმინაცია და შოუ)

### BLOCK 2: GOOGLE FLOW / VEO 3.1 VIDEO PROMPTS (READY TO COPY)
Provide 5 standalone, English-language prompts matching the 5 scenes above, optimized for Google Flow and Veo 3.1.

### BLOCK 3: SUNO AI SOUNDTRACK ARCHITECTURE (READY TO COPY)
Provide 2 curated soundtrack prompts:
- Option 1: Welcome & Cocktail Ambient (95-105 BPM)
- Option 2: Grand Reveal & Awards Climax (115-122 BPM)

### BLOCK 4: ELEVENLABS VOICEOVER SCRIPTS (READY TO COPY)
- Script 1 (Georgian VIP Welcome Invitation, 20-30 sec)
- Script 2 (Georgian Hall Announcement, 15 sec)
- Script 3 (English International Gala Welcome, 20 sec)</pre>

        <!-- KA PANE -->
        <pre id="prompt-master-director-ka" class="prompt-box prompt-pane bg-[#141110] p-4 sm:p-5 rounded-xl border border-brand-goldBorder text-xs text-brand-cream/90 font-mono whitespace-pre-wrap leading-relaxed max-h-[520px] overflow-y-auto"># როლი &amp; იდენტობა
შენ ხარ მთავარი კრეატიული დირექტორი, ვიზუალური სცენოგრაფი და AI სცენარისტი პრემიუმ სააგენტოსთვის "Vanilla Events" (ცნობილია ულტრა-ლუქს გალა-საღამოებით, არქიტექტურული ქორწილებითა და სამიტებით).

შენი მისიაა დამკვეთის ნებისმიერი ბრიფი, ივენთ-კონცეფცია ან დიზაინერის სტატიკური ესკიზი გადააქციო უნაკლო, წარმოებისთვის მზა მულტიმოდალურ სარეჟისორო პაკეტად:
1. სივრცითი ნარატივი &amp; 5-სცენიანი Storyboard
2. ოპტიკური Image-to-Video (I2V) პრომპტები Google Flow / Veo 3.1 და Runway Gen-3-ისთვის
3. აკუსტიკური არქიტექტურა &amp; მუსიკალური დირექტივები Suno AI-სთვის
4. ემოციური ხმოვანი სცენარები ElevenLabs-ისთვის (ქართულ და ინგლისურ ენებზე)

# VANILLA EVENTS-ის ლუქს-დიზაინის ესთეტიკური კოდი (მკაცრი წესები)
ნებისმიერი ვიზუალური, სივრცითი თუ აუდიო დირექტივის შექმნისას მკაცრად დაიცავი Vanilla Events-ის ფილოსოფია:
1. ფერთა პალიტრა: შავი გაპრიალებული მარმარილო, მატი სპილოსძვლისფერი, ღრმა ზურმუხტისფერი ხავერდი, დავარგებული შამპანურის ბრინჯაო და თბილი ოქროს აქცენტები.
2. განათების ფილოსოფია: არასდროს გამოიყენო უხეში თეთრი ან ბრტყელი ფლუორესცენტული შუქი. გამოიყენე თბილი 2700K სანთლის ქარვისფერი ნათება, 3200K კედლის არქიტექტურული განათება, მიმართული რბილი აქცენტები ყვავილებზე და 5600K მთვარის შუქის კონტურები.
3. ფლორისტიკა &amp; დეკორი: მონუმენტური არქიტექტურული კონსტრუქციები, კასკადური თეთრი ფალაენოპსისის ორქიდეები, ბაღის ვარდები, ზეთისხილის ტოტები, ბროლის პრიზმები და მაღალი სანთლები.
4. მოძრაობის ფილოსოფია: ულტრა-რბილი, გააზრებული, დიდებული კინემატოგრაფიული მოძრაობა. ნული სწრაფი ჭრა, ნული კამერის კანკალი, ნული დეფორმაცია (Warping). მოძრაობის ინტენსივობა 2-4 / 10.
5. სტოკ-კლიშეების აკრძალვა: არავითარი ქაოტური ხალხმრავლობა, არავითარი პლასტმასის ბუშტების თაღები, არავითარი იაფი ფერადი დისკო-შუქები.

# პრომპტების გენერაციის ძრავები

## ძრავი A: IMAGE-TO-VIDEO (GOOGLE FLOW / VEO 3.1 / RUNWAY GEN-3)
ვიდეო პრომპტისთვის დაიცავი ზუსტი სამეცნიერო სტრუქტურა:
- [კამერა და ობიექტივი]: "Cinematic slow [push-in / 45-degree orbit / pedestal crane / lateral pan], filmed on Arri Alexa Mini LF, [35mm / 50mm / anamorphic] lens, f/2.0 aperture, shallow depth of field, 24fps cinema look..."
- [სუბიექტი და გარემო]: Vanilla Events-ის კონკრეტული სცენა (მაგიდები, ფასადი, სცენა, ფოტოზონა).
- [გარემოს დინამიკა]: სანთლების ნაზი ციმციმი (2700K), მსუბუქი ნიავი ორქიდეის ფურცლებზე, მშრალი ყინულის ნისლი იატაკზე 0.5 მ/წმ სიჩქარით.
- [შესრულების პარამეტრები]: "Ultra-realistic 8k, stable motion, zero camera jitter, zero warping, photorealistic luxury event design."

## ძრავი B: SUNO AI მუსიკალური დირექტივები
ივენთის მუსიკისთვის მოაწოდე სტრუქტურული პრომპტი ზუსტი ჟანრით, BPM-ით და ინსტრუმენტებით:
- ფორმატი: [Style: ზუსტი ჟანრი, BPM: ზუსტი რიცხვი, ინსტრუმენტები, ატმოსფერო, instrumental only, no vocals]
- სტრუქტურული თეგები: [Intro], [Ambient Piano Theme], [Subtle Strings Build], [Harmonic Climax], [Outro Fade]
- წესი: ყოველთვის მიუთითე "[instrumental only, no vocals]", თუ საპირისპირო პირდაპირ არ მოგეთხოვება.

## ძრავი C: ELEVENLABS ხმოვანი დირექტივები
საზეიმო ანონსებისა და მოსაწვევებისთვის:
- ტონი: ხავერდოვანი, თბილი, პრესტიჟული, გაზომილი რიტმი, ბუნებრივი სუნთქვა.
- მოაწოდე 2 ვერსია: ელიტური ქართული და საერთაშორისო ინგლისური.
- გამოიყენე ელიფსისი (...) 0.5-წამიანი ბუნებრივი პაუზებისთვის და ემოციური მინიშნებები: [warm welcoming tone], [solemn celebratory pause].

# სტანდარტული გამომავალი სქემა
ყოველთვის გამოიტანე შემდეგი 4 სტრუქტურული ბლოკი:
ბლოკი 1: ივენთის ნარატივი &amp; 5-სცენიანი Storyboard
ბლოკი 2: Google Flow / Veo 3.1 ვიდეო პრომპტები (მზად კოპირებისთვის)
ბლოკი 3: Suno AI საუნდტრეკის არქიტექტურა (2 ვარიანტი: Cocktail &amp; Climax)
ბლოკი 4: ElevenLabs ხმოვანი სკრიპტები (ქართული და ინგლისური)</pre>
      </div>'''

assert old_master_prompt_block in html, "Master prompt block not found"
html = html.replace(old_master_prompt_block, new_master_prompt_block)
print("Master prompt converted to bilingual.")

# 2. BILINGUAL SPECIALIZED PROMPTS (CAMERA OPTIMIZER & AUDIO ARCHITECT)
old_spec_prompts = '''        <!-- Specialized Prompt 1: Camera Motion Optimizer -->
        <div class="vanilla-card p-5 space-y-3 border border-brand-goldBorder/70">
          <div class="flex items-center justify-between">
            <span class="text-[10px] uppercase font-bold text-brand-gold tracking-wider">სპეციალიზებული სისტემური პრომპტი 02</span>
            <button onclick="copyPromptText('prompt-camera-optimizer')" id="btn-prompt-camera-optimizer" class="bronze-btn px-3 py-1 rounded-full text-[10px] font-semibold uppercase">კოპირება</button>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">Camera Motion Optimizer &amp; Anti-Warping Expert</h4>
          <p class="text-xs text-brand-cream/80 font-light leading-relaxed">
            დამხმარე ასისტენტი, რომელიც ამოწმებს უკვე დაწერილ ვიდეო პრომპტს, ასწორებს დეფორმაციის გამომწვევ შეცდომებს და გარდაქმნის მას სტაბილურ კინემატოგრაფიულ კოდად.
          </p>
          <pre id="prompt-camera-optimizer" class="prompt-box bg-[#141110] p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed max-h-48 overflow-y-auto">You are a Senior Cinematography & Prompt Optimization Specialist for Runway Gen-3 and Google Flow Veo 3.1.
When given a raw video prompt that produced camera warping, facial distortion, or jitter:
1. Strip away conflicting multiple camera movements. Enforce ONE single clean vector (e.g., pure Slow Push-in OR pure 45-degree Orbit).
2. Add explicit physics damping constraints: "slow constant camera velocity, zero acceleration, zero warping, stable architectural geometry, locked perspective".
3. Lower motion intensity to 3/10 and set lens to 35mm cinema prime.
Output the revised, production-ready prompt immediately.</pre>
        </div>

        <!-- Specialized Prompt 2: Audio & Voice Director -->
        <div class="vanilla-card p-5 space-y-3 border border-brand-goldBorder/70">
          <div class="flex items-center justify-between">
            <span class="text-[10px] uppercase font-bold text-brand-gold tracking-wider">სპეციალიზებული სისტემური პრომპტი 03</span>
            <button onclick="copyPromptText('prompt-audio-voice-director')" id="btn-prompt-audio-voice-director" class="bronze-btn px-3 py-1 rounded-full text-[10px] font-semibold uppercase">კოპირება</button>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">Event Audio Scenographer &amp; Voiceover Architect</h4>
          <p class="text-xs text-brand-cream/80 font-light leading-relaxed">
            ასისტენტი, რომელიც სპეციალიზებულია ივენთის აკუსტიკურ დრამატურგიაზე, მუსიკალური ტემპის (BPM) ზუსტ გათვლასა და ქართული ხმოვანი სცენარების ინტონაციურ დამუშავებაზე.
          </p>
          <pre id="prompt-audio-voice-director" class="prompt-box bg-[#141110] p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed max-h-48 overflow-y-auto">You are the Sound Designer and Voiceover Director for Vanilla Events.
When given an event vibe and schedule:
1. Calculate the exact musical progression: Cocktail (95-102 BPM Organic Lounge), Dinner (75-85 BPM Acoustic Classical), Awards/Reveal (116-122 BPM Hybrid Orchestral).
2. Generate ready-to-paste Suno prompts with negative tags to guarantee pure instrumental tracks.
3. Write high-class Georgian and English voice scripts with SSML pauses [pause: 0.5s] and pronunciation notes for luxury brands.</pre>
        </div>'''

new_spec_prompts = '''        <!-- Specialized Prompt 1: Camera Motion Optimizer (BILINGUAL) -->
        <div class="vanilla-card p-5 space-y-3 border border-brand-goldBorder/70">
          <div class="flex flex-wrap items-center justify-between gap-2">
            <span class="text-[10px] uppercase font-bold text-brand-gold tracking-wider">სპეციალიზებული სისტემური პრომპტი 02</span>
            <div class="flex items-center gap-1.5">
              <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                <button onclick="setPromptLang('prompt-camera-optimizer', 'en')" id="tab-prompt-camera-optimizer-en" class="prompt-lang-tab active-tab">EN</button>
                <button onclick="setPromptLang('prompt-camera-optimizer', 'ka')" id="tab-prompt-camera-optimizer-ka" class="prompt-lang-tab">GEO</button>
              </div>
              <button onclick="copyBilingualPrompt('prompt-camera-optimizer')" id="btn-prompt-camera-optimizer" class="bronze-btn px-3 py-1 rounded-full text-[10px] font-semibold uppercase">კოპირება</button>
            </div>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">Camera Motion Optimizer &amp; Anti-Warping Expert</h4>
          <p class="text-xs text-brand-cream/80 font-light leading-relaxed">
            დამხმარე ასისტენტი, რომელიც ამოწმებს უკვე დაწერილ ვიდეო პრომპტს, ასწორებს დეფორმაციის გამომწვევ შეცდომებს და გარდაქმნის მას სტაბილურ კინემატოგრაფიულ კოდად.
          </p>
          <pre id="prompt-camera-optimizer-en" class="prompt-box prompt-pane active-pane bg-[#141110] p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed max-h-48 overflow-y-auto">You are a Senior Cinematography & Prompt Optimization Specialist for Runway Gen-3 and Google Flow Veo 3.1.
When given a raw video prompt that produced camera warping, facial distortion, or jitter:
1. Strip away conflicting multiple camera movements. Enforce ONE single clean vector (e.g., pure Slow Push-in OR pure 45-degree Orbit).
2. Add explicit physics damping constraints: "slow constant camera velocity, zero acceleration, zero warping, stable architectural geometry, locked perspective".
3. Lower motion intensity to 3/10 and set lens to 35mm cinema prime.
Output the revised, production-ready prompt immediately.</pre>
          <pre id="prompt-camera-optimizer-ka" class="prompt-box prompt-pane bg-[#141110] p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed max-h-48 overflow-y-auto">შენ ხარ კინემატოგრაფიისა და პრომპტ-ოპტიმიზაციის წამყვანი სპეციალისტი Runway Gen-3-ისა და Google Flow Veo 3.1-ისთვის.
როდესაც მიიღებ ნედლ პრომპტს, რომელმაც გამოიწვია დეფორმაცია (Warping) ან კამერის კანკალი:
1. მოაშორე ერთმანეთთან შეუსაბამო მოძრაობები. დატოვე მხოლოდ 1 სუფთა ვექტორი (მაგ. სუფთა Slow Push-in ან სუფთა 45-გრადუსიანი Orbit).
2. დაამატე ფიზიკის სტაბილიზაციის დირექტივა: "slow constant camera velocity, zero acceleration, zero warping, stable architectural geometry, locked perspective".
3. მოძრაობის ინტენსივობა დაწიე 3/10-მდე და გამოიყენე 35mm კინოობიექტივი.
მყისიერად გამოიტანე შესწორებული, წარმოებისთვის მზა პრომპტი.</pre>
        </div>

        <!-- Specialized Prompt 2: Audio & Voice Director (BILINGUAL) -->
        <div class="vanilla-card p-5 space-y-3 border border-brand-goldBorder/70">
          <div class="flex flex-wrap items-center justify-between gap-2">
            <span class="text-[10px] uppercase font-bold text-brand-gold tracking-wider">სპეციალიზებული სისტემური პრომპტი 03</span>
            <div class="flex items-center gap-1.5">
              <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                <button onclick="setPromptLang('prompt-audio-voice-director', 'en')" id="tab-prompt-audio-voice-director-en" class="prompt-lang-tab active-tab">EN</button>
                <button onclick="setPromptLang('prompt-audio-voice-director', 'ka')" id="tab-prompt-audio-voice-director-ka" class="prompt-lang-tab">GEO</button>
              </div>
              <button onclick="copyBilingualPrompt('prompt-audio-voice-director')" id="btn-prompt-audio-voice-director" class="bronze-btn px-3 py-1 rounded-full text-[10px] font-semibold uppercase">კოპირება</button>
            </div>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">Event Audio Scenographer &amp; Voiceover Architect</h4>
          <p class="text-xs text-brand-cream/80 font-light leading-relaxed">
            ასისტენტი, რომელიც სპეციალიზებულია ივენთის აკუსტიკურ დრამატურგიაზე, მუსიკალური ტემპის (BPM) ზუსტ გათვლასა და ქართული ხმოვანი სცენარების ინტონაციურ დამუშავებაზე.
          </p>
          <pre id="prompt-audio-voice-director-en" class="prompt-box prompt-pane active-pane bg-[#141110] p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed max-h-48 overflow-y-auto">You are the Sound Designer and Voiceover Director for Vanilla Events.
When given an event vibe and schedule:
1. Calculate the exact musical progression: Cocktail (95-102 BPM Organic Lounge), Dinner (75-85 BPM Acoustic Classical), Awards/Reveal (116-122 BPM Hybrid Orchestral).
2. Generate ready-to-paste Suno prompts with negative tags to guarantee pure instrumental tracks.
3. Write high-class Georgian and English voice scripts with SSML pauses [pause: 0.5s] and pronunciation notes for luxury brands.</pre>
          <pre id="prompt-audio-voice-director-ka" class="prompt-box prompt-pane bg-[#141110] p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed max-h-48 overflow-y-auto">შენ ხარ Vanilla Events-ის ხმის დიზაინერი და Voiceover-ის რეჟისორი.
როდესაც მიიღებ ივენთის განწყობასა და განრიგს:
1. გამოთვალე ზუსტი მუსიკალური პროგრესია: Cocktail (95-102 BPM Organic Lounge), Dinner (75-85 BPM Acoustic Classical), Awards/Reveal (116-122 BPM Hybrid Orchestral).
2. შექმენი Suno-ს მზა პრომპტები უარყოფითი თეგებით (negative tags), რათა გარანტირებული იყოს სუფთა ინსტრუმენტული ჟღერადობა.
3. დაწერე ელიტური ქართული და ინგლისური ხმოვანი ტექსტები SSML პაუზებით [pause: 0.5s] და გამოთქმის მითითებებით პრემიუმ ბრენდებისთვის.</pre>
        </div>'''

assert old_spec_prompts in html, "Specialized prompts not found"
html = html.replace(old_spec_prompts, new_spec_prompts)
print("Specialized prompts converted to bilingual.")

# 3. BILINGUAL FLOW PROMPTS 1-4
old_flow_prompts = '''        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          
          <!-- Prompt Case 1: Gala Push-In -->
          <div class="vanilla-card p-5 space-y-2.5 border border-brand-gold/40">
            <div class="flex items-center justify-between">
              <span class="text-[10px] uppercase font-bold text-brand-gold tracking-wider">ქეისი 01: Gala Dinner (Slow Push-in)</span>
              <button onclick="copyPromptText('prompt-flow-1')" id="btn-prompt-flow-1" class="bronze-btn px-3 py-1 rounded-full text-[10px] font-semibold uppercase">კოპირება</button>
            </div>
            <h4 class="text-xs sm:text-sm font-bold text-white">შავი მარმარილოს მაგიდები, თეთრი ორქიდეები &amp; სანთლები</h4>
            <pre id="prompt-flow-1" class="prompt-box p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">Cinematic slow push-in shot of a luxury gala dinner table setting by Vanilla Events. Camera glides smoothly forward at eye-level across mirror-polished black marble tables. Hundreds of slim ivory taper candles flicker gently with warm 2700K golden amber glow. Lush tall floral arches of white garden roses and cascading orchids sway subtly in a gentle indoor breeze. Crystal chandeliers overhead shimmer with subtle light refractions. Soft atmospheric haze and gentle dry-ice mist rolling slowly on the floor. Photorealistic 8k, filmed on Arri Alexa Mini LF, 35mm lens, f/2.0 aperture, shallow depth of field, 24fps cinema look, zero camera jitter, ultra-smooth motion.</pre>
          </div>

          <!-- Prompt Case 2: Wedding Arch Orbit -->
          <div class="vanilla-card p-5 space-y-2.5 border border-brand-gold/40">
            <div class="flex items-center justify-between">
              <span class="text-[10px] uppercase font-bold text-brand-gold tracking-wider">ქეისი 02: Outdoor Wedding (Orbit 45°)</span>
              <button onclick="copyPromptText('prompt-flow-2')" id="btn-prompt-flow-2" class="bronze-btn px-3 py-1 rounded-full text-[10px] font-semibold uppercase">კოპირება</button>
            </div>
            <h4 class="text-xs sm:text-sm font-bold text-white">შატო მუხრანი: საქორწინო თაღი &amp; მზის ჩასვლა</h4>
            <pre id="prompt-flow-2" class="prompt-box p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">Smooth 45-degree orbit arc shot around an architectural floral wedding arch at Chateau Mukhrani outdoor courtyard by Vanilla Events. Abundant white hydrangeas, blush garden roses and olive branches. Golden hour sunset light filtering through vineyards in background creating warm rim lighting and natural subtle lens flares. White rose petals on stone pavement moving softly in breeze. Ultra-realistic 8k, 35mm anamorphic lens, cinema grade, gentle wind physics, motion intensity 3, zero warp.</pre>
          </div>

          <!-- Prompt Case 3: Stage LED Reveal -->
          <div class="vanilla-card p-5 space-y-2.5 border border-brand-gold/40">
            <div class="flex items-center justify-between">
              <span class="text-[10px] uppercase font-bold text-brand-gold tracking-wider">ქეისი 03: Tech Summit Stage (Pedestal Up)</span>
              <button onclick="copyPromptText('prompt-flow-3')" id="btn-prompt-flow-3" class="bronze-btn px-3 py-1 rounded-full text-[10px] font-semibold uppercase">კოპირება</button>
            </div>
            <h4 class="text-xs sm:text-sm font-bold text-white">სცენოგრაფია: ამაღლებული კამერა &amp; LED ატმოსფერო</h4>
            <pre id="prompt-flow-3" class="prompt-box p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">Smooth pedestal crane shot moving upward from podium level to reveal a futuristic luxury corporate summit stage designed by Vanilla Events. Curved ultra-wide seamless LED backdrop displaying ambient liquid gold particles undulating slowly. Two vertical lighting towers cast sharp narrow amber shafts through light haze. Glossy black stage floor reflects lighting perfectly. Steady gimbal movement, 24mm wide-angle lens, crisp depth, high-tech elegance, 4k 24fps.</pre>
          </div>

          <!-- Prompt Case 4: Photozone Details -->
          <div class="vanilla-card p-5 space-y-2.5 border border-brand-gold/40">
            <div class="flex items-center justify-between">
              <span class="text-[10px] uppercase font-bold text-brand-gold tracking-wider">ქეისი 04: VIP Photozone (Slow Lateral Pan)</span>
              <button onclick="copyPromptText('prompt-flow-4')" id="btn-prompt-flow-4" class="bronze-btn px-3 py-1 rounded-full text-[10px] font-semibold uppercase">კოპირება</button>
            </div>
            <h4 class="text-xs sm:text-sm font-bold text-white">პრეს-ვოლი &amp; ფოტოზონა: ხავერდი, ოქრო და ყვავილები</h4>
            <pre id="prompt-flow-4" class="prompt-box p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">Slow horizontal tracking lateral pan across a VIP gala photozone by Vanilla Events. Deep emerald velvet backdrop accented with brushed brass geometric pillars and asymmetrical cascades of white phalaenopsis orchids. Soft studio flash modeling lights create gentle highlights on gold metal surfaces. Red carpet floor edge, impeccable luxury event styling, 50mm portrait lens, shallow depth of field, ultra-sharp textures, zero artifacts.</pre>
          </div>

        </div>'''

new_flow_prompts = '''        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          
          <!-- Prompt Case 1: Gala Push-In (BILINGUAL) -->
          <div class="vanilla-card p-5 space-y-2.5 border border-brand-gold/40">
            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="text-[10px] uppercase font-bold text-brand-gold tracking-wider">ქეისი 01: Gala Dinner (Slow Push-in)</span>
              <div class="flex items-center gap-1.5">
                <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                  <button onclick="setPromptLang('prompt-flow-1', 'en')" id="tab-prompt-flow-1-en" class="prompt-lang-tab active-tab">EN</button>
                  <button onclick="setPromptLang('prompt-flow-1', 'ka')" id="tab-prompt-flow-1-ka" class="prompt-lang-tab">GEO</button>
                </div>
                <button onclick="copyBilingualPrompt('prompt-flow-1')" id="btn-prompt-flow-1" class="bronze-btn px-3 py-1 rounded-full text-[10px] font-semibold uppercase">კოპირება</button>
              </div>
            </div>
            <h4 class="text-xs sm:text-sm font-bold text-white">შავი მარმარილოს მაგიდები, თეთრი ორქიდეები &amp; სანთლები</h4>
            <pre id="prompt-flow-1-en" class="prompt-box prompt-pane active-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">Cinematic slow push-in shot of a luxury gala dinner table setting by Vanilla Events. Camera glides smoothly forward at eye-level across mirror-polished black marble tables. Hundreds of slim ivory taper candles flicker gently with warm 2700K golden amber glow. Lush tall floral arches of white garden roses and cascading orchids sway subtly in a gentle indoor breeze. Crystal chandeliers overhead shimmer with subtle light refractions. Soft atmospheric haze and gentle dry-ice mist rolling slowly on the floor. Photorealistic 8k, filmed on Arri Alexa Mini LF, 35mm lens, f/2.0 aperture, shallow depth of field, 24fps cinema look, zero camera jitter, ultra-smooth motion.</pre>
            <pre id="prompt-flow-1-ka" class="prompt-box prompt-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">კინემატოგრაფიული ნელი წინსვლის (Slow Push-in) კადრი Vanilla Events-ის გალა-ვახშმის მაგიდებზე. კამერა შეუფერხებლად სრიალებს თვალის სიმაღლეზე გაპრიალებულ შავ მარმარილოზე. ასობით წვრილი სპილოსძვლისფერი სანთელი ნაზად ციმციმებს თბილი 2700K ოქროსფერ-ქარვისფერი ნათებით. თეთრი ბაღის ვარდებისა და ორქიდეების მაღალი თაღები ოდნავ ირხევა მსუბუქ ნიავში. ბროლის ჭაღები ზემოთ ირეკლავს სინათლის პრიზმებს. იატაკზე ნელა მოძრავი მშრალი ყინულის ნისლი. გადაღებულია Arri Alexa Mini LF-ზე, 35mm ობიექტივი, f/2.0 დიაფრაგმა, 24fps კინოკადრი, ნული კანკალი, სრული სტაბილურობა.</pre>
          </div>

          <!-- Prompt Case 2: Wedding Arch Orbit (BILINGUAL) -->
          <div class="vanilla-card p-5 space-y-2.5 border border-brand-gold/40">
            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="text-[10px] uppercase font-bold text-brand-gold tracking-wider">ქეისი 02: Outdoor Wedding (Orbit 45°)</span>
              <div class="flex items-center gap-1.5">
                <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                  <button onclick="setPromptLang('prompt-flow-2', 'en')" id="tab-prompt-flow-2-en" class="prompt-lang-tab active-tab">EN</button>
                  <button onclick="setPromptLang('prompt-flow-2', 'ka')" id="tab-prompt-flow-2-ka" class="prompt-lang-tab">GEO</button>
                </div>
                <button onclick="copyBilingualPrompt('prompt-flow-2')" id="btn-prompt-flow-2" class="bronze-btn px-3 py-1 rounded-full text-[10px] font-semibold uppercase">კოპირება</button>
              </div>
            </div>
            <h4 class="text-xs sm:text-sm font-bold text-white">შატო მუხრანი: საქორწინო თაღი &amp; მზის ჩასვლა</h4>
            <pre id="prompt-flow-2-en" class="prompt-box prompt-pane active-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">Smooth 45-degree orbit arc shot around an architectural floral wedding arch at Chateau Mukhrani outdoor courtyard by Vanilla Events. Abundant white hydrangeas, blush garden roses and olive branches. Golden hour sunset light filtering through vineyards in background creating warm rim lighting and natural subtle lens flares. White rose petals on stone pavement moving softly in breeze. Ultra-realistic 8k, 35mm anamorphic lens, cinema grade, gentle wind physics, motion intensity 3, zero warp.</pre>
            <pre id="prompt-flow-2-ka" class="prompt-box prompt-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">რბილი 45-გრადუსიანი წრიული (Orbit Arc) კადრი Vanilla Events-ის საქორწინო არქიტექტურული ყვავილოვანი თაღის გარშემო შატო მუხრანის ღია ეზოში. უხვი თეთრი ჰორტენზიები, ბაღის ვარდები და ზეთისხილის ტოტები. მზის ჩასვლის ოქროსფერი შუქი იფილტრება ვენახებიდან და ქმნის თბილ კონტურულ ნათებასა და ნაზ ლინზის ანარეკლებს. ქვის ფილებზე მიმოფანტული თეთრი ფურცლები ირხევა ნიავში. ულტრა-რეალისტური 8k, 35mm ანამორფული ობიექტივი, ქარის რბილი ფიზიკა, მოძრაობის ინტენსივობა 3, ნული დეფორმაცია.</pre>
          </div>

          <!-- Prompt Case 3: Stage LED Reveal (BILINGUAL) -->
          <div class="vanilla-card p-5 space-y-2.5 border border-brand-gold/40">
            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="text-[10px] uppercase font-bold text-brand-gold tracking-wider">ქეისი 03: Tech Summit Stage (Pedestal Up)</span>
              <div class="flex items-center gap-1.5">
                <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                  <button onclick="setPromptLang('prompt-flow-3', 'en')" id="tab-prompt-flow-3-en" class="prompt-lang-tab active-tab">EN</button>
                  <button onclick="setPromptLang('prompt-flow-3', 'ka')" id="tab-prompt-flow-3-ka" class="prompt-lang-tab">GEO</button>
                </div>
                <button onclick="copyBilingualPrompt('prompt-flow-3')" id="btn-prompt-flow-3" class="bronze-btn px-3 py-1 rounded-full text-[10px] font-semibold uppercase">კოპირება</button>
              </div>
            </div>
            <h4 class="text-xs sm:text-sm font-bold text-white">სცენოგრაფია: ამაღლებული კამერა &amp; LED ატმოსფერო</h4>
            <pre id="prompt-flow-3-en" class="prompt-box prompt-pane active-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">Smooth pedestal crane shot moving upward from podium level to reveal a futuristic luxury corporate summit stage designed by Vanilla Events. Curved ultra-wide seamless LED backdrop displaying ambient liquid gold particles undulating slowly. Two vertical lighting towers cast sharp narrow amber shafts through light haze. Glossy black stage floor reflects lighting perfectly. Steady gimbal movement, 24mm wide-angle lens, crisp depth, high-tech elegance, 4k 24fps.</pre>
            <pre id="prompt-flow-3-ka" class="prompt-box prompt-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">რბილი ვერტიკალური ამაღლების (Pedestal Crane) კადრი ტრიბუნის სიმაღლიდან Vanilla Events-ის ფუტურისტული ლუქს-სამიტის სცენის გამოსაჩენად. მოხრილი ულტრა-ფართო უნაკერო LED ეკრანი, რომელზეც ნელა ტალღოვნად მოძრაობს თხევადი ოქროს ნაწილაკები. ორი ვერტიკალური სანათი კოშკი ქმნის ქარვისფერ სხივებს მსუბუქ ბოლში. სცენის შავი პრიალა იატაკი იდეალურად ირეკლავს სინათლეს. სტაბილური მოძრაობა, 24mm ფართოკუთხიანი ობიექტივი, მაღალტექნოლოგიური ელეგანტურობა, 4k 24fps.</pre>
          </div>

          <!-- Prompt Case 4: Photozone Details (BILINGUAL) -->
          <div class="vanilla-card p-5 space-y-2.5 border border-brand-gold/40">
            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="text-[10px] uppercase font-bold text-brand-gold tracking-wider">ქეისი 04: VIP Photozone (Slow Lateral Pan)</span>
              <div class="flex items-center gap-1.5">
                <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                  <button onclick="setPromptLang('prompt-flow-4', 'en')" id="tab-prompt-flow-4-en" class="prompt-lang-tab active-tab">EN</button>
                  <button onclick="setPromptLang('prompt-flow-4', 'ka')" id="tab-prompt-flow-4-ka" class="prompt-lang-tab">GEO</button>
                </div>
                <button onclick="copyBilingualPrompt('prompt-flow-4')" id="btn-prompt-flow-4" class="bronze-btn px-3 py-1 rounded-full text-[10px] font-semibold uppercase">კოპირება</button>
              </div>
            </div>
            <h4 class="text-xs sm:text-sm font-bold text-white">პრეს-ვოლი &amp; ფოტოზონა: ხავერდი, ოქრო და ყვავილები</h4>
            <pre id="prompt-flow-4-en" class="prompt-box prompt-pane active-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">Slow horizontal tracking lateral pan across a VIP gala photozone by Vanilla Events. Deep emerald velvet backdrop accented with brushed brass geometric pillars and asymmetrical cascades of white phalaenopsis orchids. Soft studio flash modeling lights create gentle highlights on gold metal surfaces. Red carpet floor edge, impeccable luxury event styling, 50mm portrait lens, shallow depth of field, ultra-sharp textures, zero artifacts.</pre>
            <pre id="prompt-flow-4-ka" class="prompt-box prompt-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">ნელი ჰორიზონტალური გვერდითი მოძრაობის (Lateral Pan) კადრი Vanilla Events-ის VIP გალა-ფოტოზონის გასწვრივ. ღრმა ზურმუხტისფერი ხავერდის ფონი დავარგებული თითბრის გეომეტრიული სვეტებითა და თეთრი ორქიდეების ასიმეტრიული კასკადებით. რბილი სტუდიური განათება ქმნის ელეგანტურ ანარეკლებს ოქროსფერ მეტალზე. წითელი ხალიჩის კიდე, უნაკლო ლუქს-სტილი, 50mm პორტრეტული ობიექტივი, ფოკუსის რბილი სიღრმე, კრისტალურად სუფთა ტექსტურა.</pre>
          </div>

        </div>'''

assert old_flow_prompts in html, "Flow prompts not found"
html = html.replace(old_flow_prompts, new_flow_prompts)
print("Flow prompts converted to bilingual.")

# 4. BILINGUAL SUNO & ELEVENLABS PROMPTS
old_suno_eleven = '''          <!-- Suno Prompt Templates -->
          <div class="space-y-3 pt-1">
            <div class="sub-surface p-3.5 rounded-xl border border-brand-goldBorder space-y-1.5">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-white">ქეისი 1: Cocktail Lounge &amp; Welcome (102 BPM)</span>
                <button onclick="copyPromptText('prompt-suno-1')" id="btn-prompt-suno-1" class="text-brand-gold hover:underline text-[11px] font-bold">კოპირება</button>
              </div>
              <pre id="prompt-suno-1" class="prompt-box p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">[Style: Luxury Gala Lounge, Organic Deep House, 102 BPM, warm Rhodes piano, gentle cello pads, subtle analog shaker percussion, elegant, sophisticated, atmospheric, instrumental only, no vocals, high-end production]</pre>
            </div>

            <div class="sub-surface p-3.5 rounded-xl border border-brand-goldBorder space-y-1.5">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-white">ქეისი 2: Awards &amp; Grand Reveal (118 BPM)</span>
                <button onclick="copyPromptText('prompt-suno-2')" id="btn-prompt-suno-2" class="text-brand-gold hover:underline text-[11px] font-bold">კოპირება</button>
              </div>
              <pre id="prompt-suno-2" class="prompt-box p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">[Style: Cinematic Hybrid Orchestral, 118 BPM, Hans Zimmer style, brass crescendos, driving electronic pulse, triumphant strings, luxury corporate gala awards ceremony opening, energetic, prestigious, instrumental only]</pre>
            </div>

            <div class="sub-surface p-3.5 rounded-xl border border-brand-goldBorder space-y-1.5">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-white">ქეისი 3: Luxury Wedding Entrance (78 BPM)</span>
                <button onclick="copyPromptText('prompt-suno-3')" id="btn-prompt-suno-3" class="text-brand-gold hover:underline text-[11px] font-bold">კოპირება</button>
              </div>
              <pre id="prompt-suno-3" class="prompt-box p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">[Style: Romantic Neo-Classical Acoustic, 78 BPM, emotional live cello, concert harp, soft Steinway grand piano, gentle room reverb, fairytale royal wedding ceremony entrance, breathtaking, timeless, instrumental only]</pre>
            </div>
          </div>
        </div>

        <!-- ElevenLabs Card -->
        <div class="vanilla-card p-5 sm:p-6 space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="serif-font text-base sm:text-lg font-bold text-white flex items-center gap-2">
              <span class="text-brand-gold">🎙️</span> ElevenLabs: Eleven v3 &amp; Flash v2.5
            </h3>
            <span class="px-2 py-0.5 rounded-full badge-pill border border-brand-goldBorder text-[10px] font-bold">Georgian &amp; English</span>
          </div>
          <p class="text-xs sm:text-sm text-brand-cream/80 font-light leading-relaxed">
            <strong>Eleven v3</strong> არის Voice AI-ის ოქროს სტანდარტი მსახიობური ემოციური დიაპაზონით, 70+ ენითა და inline ემოციური ტეგებით: <code>[whispers]</code>, <code>[laughs]</code>, <code>[warm welcoming tone]</code>. <strong>Flash v2.5</strong> უზრუნველყოფს 75ms მოდელის ინფერენსს. დიზაინერს შეუძლია ვიდეო-რენდერს ან ციფრულ მოსაწვევს დაადოს უმაღლესი დონის ხმა:
          </p>

          <!-- ElevenLabs Script Templates -->
          <div class="space-y-3 pt-1">
            <div class="sub-surface p-3.5 rounded-xl border border-brand-goldBorder space-y-1.5">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-white">ქეისი 1: VIP ხმოვანი მოსაწვევი (ქართული)</span>
                <button onclick="copyPromptText('prompt-eleven-1')" id="btn-prompt-eleven-1" class="text-brand-gold hover:underline text-[11px] font-bold">კოპირება</button>
              </div>
              <pre id="prompt-eleven-1" class="prompt-box p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">მოგესალმებით. Vanilla Events მოხარულია გიხილოთ წლის მთავარ გალა-საღამოზე. გთხოვთ გადახვიდეთ თქვენს პირად ბმულზე და დაადასტუროთ დასწრება. თქვენ გელით დაუვიწყარი ატმოსფერო, ექსკლუზიური მუსიკალური პროგრამა და განსაკუთრებული სივრცე.</pre>
            </div>

            <div class="sub-surface p-3.5 rounded-xl border border-brand-goldBorder space-y-1.5">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-white">ქეისი 2: ოფიციალური დარბაზის ანონსი (ქართული)</span>
                <button onclick="copyPromptText('prompt-eleven-2')" id="btn-prompt-eleven-2" class="text-brand-gold hover:underline text-[11px] font-bold">კოპირება</button>
              </div>
              <pre id="prompt-eleven-2" class="prompt-box p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">ქალბატონებო და ბატონებო, საღამოს ოფიციალური ცერემონია და დაჯილდოება დაიწყება 5 წუთში. გთხოვთ მობრძანდეთ მთავარ დარბაზში და დაიკავოთ თქვენი ადგილები.</pre>
            </div>

            <div class="sub-surface p-3.5 rounded-xl border border-brand-goldBorder space-y-1.5">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-white">ქეისი 3: International VIP Gala (English)</span>
                <button onclick="copyPromptText('prompt-eleven-3')" id="btn-prompt-eleven-3" class="text-brand-gold hover:underline text-[11px] font-bold">კოპირება</button>
              </div>
              <pre id="prompt-eleven-3" class="prompt-box p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">Good evening and welcome. Vanilla Events is honored to present tonight's Annual Innovation Gala. We invite you to experience an extraordinary evening of architectural elegance, gourmet culinary artistry, and celebration. Please proceed to your tables.</pre>
            </div>
          </div>'''

new_suno_eleven = '''          <!-- Suno Prompt Templates (BILINGUAL) -->
          <div class="space-y-3 pt-1">
            <div class="sub-surface p-3.5 rounded-xl border border-brand-goldBorder space-y-1.5">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-bold text-white">ქეისი 1: Cocktail Lounge &amp; Welcome (102 BPM)</span>
                <div class="flex items-center gap-1.5">
                  <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                    <button onclick="setPromptLang('prompt-suno-1', 'en')" id="tab-prompt-suno-1-en" class="prompt-lang-tab active-tab">EN</button>
                    <button onclick="setPromptLang('prompt-suno-1', 'ka')" id="tab-prompt-suno-1-ka" class="prompt-lang-tab">GEO</button>
                  </div>
                  <button onclick="copyBilingualPrompt('prompt-suno-1')" id="btn-prompt-suno-1" class="text-brand-gold hover:underline text-[11px] font-bold">კოპირება</button>
                </div>
              </div>
              <pre id="prompt-suno-1-en" class="prompt-box prompt-pane active-pane p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">[Style: Luxury Gala Lounge, Organic Deep House, 102 BPM, warm Rhodes piano, gentle cello pads, subtle analog shaker percussion, elegant, sophisticated, atmospheric, instrumental only, no vocals, high-end production]</pre>
              <pre id="prompt-suno-1-ka" class="prompt-box prompt-pane p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">[სტილი: ლუქს გალა ლაუნჯი, ორგანული დიპ ჰაუსი, 102 BPM, თბილი როდს პიანინო, ნაზი ჩელო, ანალოგური პერკუსია, ელეგანტური, ატმოსფერული, მხოლოდ ინსტრუმენტული, ვოკალის გარეშე, სტუდიური ხარისხი]</pre>
            </div>

            <div class="sub-surface p-3.5 rounded-xl border border-brand-goldBorder space-y-1.5">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-bold text-white">ქეისი 2: Awards &amp; Grand Reveal (118 BPM)</span>
                <div class="flex items-center gap-1.5">
                  <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                    <button onclick="setPromptLang('prompt-suno-2', 'en')" id="tab-prompt-suno-2-en" class="prompt-lang-tab active-tab">EN</button>
                    <button onclick="setPromptLang('prompt-suno-2', 'ka')" id="tab-prompt-suno-2-ka" class="prompt-lang-tab">GEO</button>
                  </div>
                  <button onclick="copyBilingualPrompt('prompt-suno-2')" id="btn-prompt-suno-2" class="text-brand-gold hover:underline text-[11px] font-bold">კოპირება</button>
                </div>
              </div>
              <pre id="prompt-suno-2-en" class="prompt-box prompt-pane active-pane p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">[Style: Cinematic Hybrid Orchestral, 118 BPM, Hans Zimmer style, brass crescendos, driving electronic pulse, triumphant strings, luxury corporate gala awards ceremony opening, energetic, prestigious, instrumental only]</pre>
              <pre id="prompt-suno-2-ka" class="prompt-box prompt-pane p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">[სტილი: კინემატოგრაფიული ჰიბრიდული ორკესტრი, 118 BPM, ჰანს ციმერის სტილი, ჩასაბერების კრშენდო, ენერგიული პულსი, საზეიმო სიმებიანები, გალა დაჯილდოების გახსნა, ენერგიული, პრესტიჟული, მხოლოდ ინსტრუმენტული]</pre>
            </div>

            <div class="sub-surface p-3.5 rounded-xl border border-brand-goldBorder space-y-1.5">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-bold text-white">ქეისი 3: Luxury Wedding Entrance (78 BPM)</span>
                <div class="flex items-center gap-1.5">
                  <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                    <button onclick="setPromptLang('prompt-suno-3', 'en')" id="tab-prompt-suno-3-en" class="prompt-lang-tab active-tab">EN</button>
                    <button onclick="setPromptLang('prompt-suno-3', 'ka')" id="tab-prompt-suno-3-ka" class="prompt-lang-tab">GEO</button>
                  </div>
                  <button onclick="copyBilingualPrompt('prompt-suno-3')" id="btn-prompt-suno-3" class="text-brand-gold hover:underline text-[11px] font-bold">კოპირება</button>
                </div>
              </div>
              <pre id="prompt-suno-3-en" class="prompt-box prompt-pane active-pane p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">[Style: Romantic Neo-Classical Acoustic, 78 BPM, emotional live cello, concert harp, soft Steinway grand piano, gentle room reverb, fairytale royal wedding ceremony entrance, breathtaking, timeless, instrumental only]</pre>
              <pre id="prompt-suno-3-ka" class="prompt-box prompt-pane p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">[სტილი: რომანტიკული ნეოკლასიკური აკუსტიკა, 78 BPM, ემოციური ცოცხალი ჩელო, საკონცერტო არფა, როიალი სტეინვეი, რბილი რევერბერაცია, სამეფო ქორწილის შემოსვლა, ზღაპრული, მხოლოდ ინსტრუმენტული]</pre>
            </div>
          </div>
        </div>

        <!-- ElevenLabs Card (BILINGUAL) -->
        <div class="vanilla-card p-5 sm:p-6 space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="serif-font text-base sm:text-lg font-bold text-white flex items-center gap-2">
              <span class="text-brand-gold">🎙️</span> ElevenLabs: Eleven v3 &amp; Flash v2.5
            </h3>
            <span class="px-2 py-0.5 rounded-full badge-pill border border-brand-goldBorder text-[10px] font-bold">Georgian &amp; English</span>
          </div>
          <p class="text-xs sm:text-sm text-brand-cream/80 font-light leading-relaxed">
            <strong>Eleven v3</strong> არის Voice AI-ის ოქროს სტანდარტი მსახიობური ემოციური დიაპაზონით, 70+ ენითა და inline ემოციური ტეგებით: <code>[whispers]</code>, <code>[laughs]</code>, <code>[warm welcoming tone]</code>. <strong>Flash v2.5</strong> უზრუნველყოფს 75ms მოდელის ინფერენსს. დიზაინერს შეუძლია ვიდეო-რენდერს ან ციფრულ მოსაწვევს დაადოს უმაღლესი დონის ხმა:
          </p>

          <!-- ElevenLabs Script Templates (BILINGUAL) -->
          <div class="space-y-3 pt-1">
            <div class="sub-surface p-3.5 rounded-xl border border-brand-goldBorder space-y-1.5">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-bold text-white">ქეისი 1: VIP ხმოვანი მოსაწვევი</span>
                <div class="flex items-center gap-1.5">
                  <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                    <button onclick="setPromptLang('prompt-eleven-1', 'ka')" id="tab-prompt-eleven-1-ka" class="prompt-lang-tab active-tab">GEO</button>
                    <button onclick="setPromptLang('prompt-eleven-1', 'en')" id="tab-prompt-eleven-1-en" class="prompt-lang-tab">EN</button>
                  </div>
                  <button onclick="copyBilingualPrompt('prompt-eleven-1')" id="btn-prompt-eleven-1" class="text-brand-gold hover:underline text-[11px] font-bold">კოპირება</button>
                </div>
              </div>
              <pre id="prompt-eleven-1-ka" class="prompt-box prompt-pane active-pane p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">მოგესალმებით. Vanilla Events მოხარულია გიხილოთ წლის მთავარ გალა-საღამოზე. გთხოვთ გადახვიდეთ თქვენს პირად ბმულზე და დაადასტუროთ დასწრება. თქვენ გელით დაუვიწყარი ატმოსფერო, ექსკლუზიური მუსიკალური პროგრამა და განსაკუთრებული სივრცე.</pre>
              <pre id="prompt-eleven-1-en" class="prompt-box prompt-pane p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">Welcome. Vanilla Events is delighted to invite you to the premier gala event of the year. Please follow your personalized link to confirm your attendance. An unforgettable atmosphere, exclusive musical curation, and bespoke architectural spaces await you.</pre>
            </div>

            <div class="sub-surface p-3.5 rounded-xl border border-brand-goldBorder space-y-1.5">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-bold text-white">ქეისი 2: ოფიციალური დარბაზის ანონსი</span>
                <div class="flex items-center gap-1.5">
                  <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                    <button onclick="setPromptLang('prompt-eleven-2', 'ka')" id="tab-prompt-eleven-2-ka" class="prompt-lang-tab active-tab">GEO</button>
                    <button onclick="setPromptLang('prompt-eleven-2', 'en')" id="tab-prompt-eleven-2-en" class="prompt-lang-tab">EN</button>
                  </div>
                  <button onclick="copyBilingualPrompt('prompt-eleven-2')" id="btn-prompt-eleven-2" class="text-brand-gold hover:underline text-[11px] font-bold">კოპირება</button>
                </div>
              </div>
              <pre id="prompt-eleven-2-ka" class="prompt-box prompt-pane active-pane p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">ქალბატონებო და ბატონებო, საღამოს ოფიციალური ცერემონია და დაჯილდოება დაიწყება 5 წუთში. გთხოვთ მობრძანდეთ მთავარ დარბაზში და დაიკავოთ თქვენი ადგილები.</pre>
              <pre id="prompt-eleven-2-en" class="prompt-box prompt-pane p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">Ladies and gentlemen, tonight\'s official ceremony and awards gala will commence in five minutes. We kindly ask you to proceed into the grand ballroom and take your seats.</pre>
            </div>

            <div class="sub-surface p-3.5 rounded-xl border border-brand-goldBorder space-y-1.5">
              <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-bold text-white">ქეისი 3: International VIP Gala Welcome</span>
                <div class="flex items-center gap-1.5">
                  <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                    <button onclick="setPromptLang('prompt-eleven-3', 'en')" id="tab-prompt-eleven-3-en" class="prompt-lang-tab active-tab">EN</button>
                    <button onclick="setPromptLang('prompt-eleven-3', 'ka')" id="tab-prompt-eleven-3-ka" class="prompt-lang-tab">GEO</button>
                  </div>
                  <button onclick="copyBilingualPrompt('prompt-eleven-3')" id="btn-prompt-eleven-3" class="text-brand-gold hover:underline text-[11px] font-bold">კოპირება</button>
                </div>
              </div>
              <pre id="prompt-eleven-3-en" class="prompt-box prompt-pane active-pane p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">Good evening and welcome. Vanilla Events is honored to present tonight\'s Annual Innovation Gala. We invite you to experience an extraordinary evening of architectural elegance, gourmet culinary artistry, and celebration. Please proceed to your tables.</pre>
              <pre id="prompt-eleven-3-ka" class="prompt-box prompt-pane p-2.5 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap">საღამო მშვიდობისა და კეთილი იყოს თქვენი მობრძანება. Vanilla Events მოხარულია წარმოგიდგინოთ ყოველწლიური ინოვაციების გალა. გეპატიჟებით განიცადოთ არქიტექტურული ელეგანტურობის, გასტრონომიული ხელოვნებისა და ზეიმის არაჩვეულებრივი საღამო. გთხოვთ მიბრძანდეთ თქვენს მაგიდებთან.</pre>
            </div>
          </div>'''

assert old_suno_eleven in html, "Suno and ElevenLabs block not found"
html = html.replace(old_suno_eleven, new_suno_eleven)
print("Suno and ElevenLabs converted to bilingual.")

# 5. BILINGUAL PROMPT BANK (P-BANK-1, P-BANK-2, P-BANK-3)
old_p_bank = '''      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        
        <!-- Prompt Card 1 -->
        <div class="vanilla-card p-5 space-y-2.5">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-brand-gold uppercase">Veo 3.1: Drone Reveal</span>
            <button onclick="copyPromptText('p-bank-1')" id="btn-p-bank-1" class="text-brand-gold hover:underline font-bold text-[11px]">კოპირება</button>
          </div>
          <h4 class="text-xs font-bold text-white">ღამის ფასადი, განათება &amp; ფეიერვერკი</h4>
          <pre id="p-bank-1" class="prompt-box p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">Cinematic slow descending drone shot of an illuminated historic chateau estate at midnight by Vanilla Events. Warm golden architectural facade lighting, fireworks bursting softly in the distant velvet night sky. Reflecting pool in foreground, high aesthetic, 8k, photorealistic, 24fps cinema look.</pre>
        </div>

        <!-- Prompt Card 2 -->
        <div class="vanilla-card p-5 space-y-2.5">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-brand-gold uppercase">Suno v6: Electronic Lounge</span>
            <button onclick="copyPromptText('p-bank-2')" id="btn-p-bank-2" class="text-brand-gold hover:underline font-bold text-[11px]">კოპირება</button>
          </div>
          <h4 class="text-xs font-bold text-white">Afterparty &amp; Night Lounge (114 BPM)</h4>
          <pre id="p-bank-2" class="prompt-box p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">[Style: Melodic Deep Techno, 114 BPM, warm analog synth arp, pulsing subdued sub-bass, airy vocal textures, luxury fashion afterparty vibe, sophisticated, late night elegance, instrumental only]</pre>
        </div>

        <!-- Prompt Card 3 -->
        <div class="vanilla-card p-5 space-y-2.5">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-brand-gold uppercase">ElevenLabs: Official Speech</span>
            <button onclick="copyPromptText('p-bank-3')" id="btn-p-bank-3" class="text-brand-gold hover:underline font-bold text-[11px]">კოპირება</button>
          </div>
          <h4 class="text-xs font-bold text-white">ოფიციალური მიმართვა სტუმრებს</h4>
          <pre id="p-bank-3" class="prompt-box p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">ძვირფასო სტუმრებო, კეთილი იყოს თქვენი მობრძანება Vanilla Events-ის საიუბილეო საღამოზე. საზეიმო ცერემონია დაიწყება რამდენიმე წუთში. გისურვებთ სასიამოვნო და შთამბეჭდავ საღამოს.</pre>
        </div>

      </div>'''

new_p_bank = '''      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        
        <!-- Prompt Card 1 (BILINGUAL) -->
        <div class="vanilla-card p-5 space-y-2.5">
          <div class="flex flex-wrap items-center justify-between gap-2 text-xs">
            <span class="font-bold text-brand-gold uppercase">Veo 3.1: Drone Reveal</span>
            <div class="flex items-center gap-1.5">
              <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                <button onclick="setPromptLang('p-bank-1', 'en')" id="tab-p-bank-1-en" class="prompt-lang-tab active-tab">EN</button>
                <button onclick="setPromptLang('p-bank-1', 'ka')" id="tab-p-bank-1-ka" class="prompt-lang-tab">GEO</button>
              </div>
              <button onclick="copyBilingualPrompt('p-bank-1')" id="btn-p-bank-1" class="text-brand-gold hover:underline font-bold text-[11px]">კოპირება</button>
            </div>
          </div>
          <h4 class="text-xs font-bold text-white">ღამის ფასადი, განათება &amp; ფეიერვერკი</h4>
          <pre id="p-bank-1-en" class="prompt-box prompt-pane active-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">Cinematic slow descending drone shot of an illuminated historic chateau estate at midnight by Vanilla Events. Warm golden architectural facade lighting, fireworks bursting softly in the distant velvet night sky. Reflecting pool in foreground, high aesthetic, 8k, photorealistic, 24fps cinema look.</pre>
          <pre id="p-bank-1-ka" class="prompt-box prompt-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">კინემატოგრაფიული ნელი დაშვების დრონის კადრი Vanilla Events-ის განათებული ისტორიული შატოს მამულზე შუაღამისას. თბილი ოქროსფერი არქიტექტურული ფასადის განათება, შორს ხავერდოვან ღამის ცაზე რბილად აფეთქებული ფეიერვერკი. წინა პლანზე წყლის ამრეკლავი აუზი, მაღალი ესთეტიკა, 8k, 24fps კინოკადრი.</pre>
        </div>

        <!-- Prompt Card 2 (BILINGUAL) -->
        <div class="vanilla-card p-5 space-y-2.5">
          <div class="flex flex-wrap items-center justify-between gap-2 text-xs">
            <span class="font-bold text-brand-gold uppercase">Suno v6: Electronic Lounge</span>
            <div class="flex items-center gap-1.5">
              <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                <button onclick="setPromptLang('p-bank-2', 'en')" id="tab-p-bank-2-en" class="prompt-lang-tab active-tab">EN</button>
                <button onclick="setPromptLang('p-bank-2', 'ka')" id="tab-p-bank-2-ka" class="prompt-lang-tab">GEO</button>
              </div>
              <button onclick="copyBilingualPrompt('p-bank-2')" id="btn-p-bank-2" class="text-brand-gold hover:underline font-bold text-[11px]">კოპირება</button>
            </div>
          </div>
          <h4 class="text-xs font-bold text-white">Afterparty &amp; Night Lounge (114 BPM)</h4>
          <pre id="p-bank-2-en" class="prompt-box prompt-pane active-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">[Style: Melodic Deep Techno, 114 BPM, warm analog synth arp, pulsing subdued sub-bass, airy vocal textures, luxury fashion afterparty vibe, sophisticated, late night elegance, instrumental only]</pre>
          <pre id="p-bank-2-ka" class="prompt-box prompt-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">[სტილი: მელოდიური დიპ ტექნო, 114 BPM, თბილი ანალოგური სინთეზატორის არპეჯიო, რბილი საბ-ბასი, ეთერული ტექსტურები, ლუქს აფთერფართის განწყობა, დახვეწილი ღამის ელეგანტურობა, მხოლოდ ინსტრუმენტული]</pre>
        </div>

        <!-- Prompt Card 3 (BILINGUAL) -->
        <div class="vanilla-card p-5 space-y-2.5">
          <div class="flex flex-wrap items-center justify-between gap-2 text-xs">
            <span class="font-bold text-brand-gold uppercase">ElevenLabs: Official Speech</span>
            <div class="flex items-center gap-1.5">
              <div class="inline-flex items-center gap-1 bg-[#141110] p-0.5 rounded-full border border-brand-goldBorder/40">
                <button onclick="setPromptLang('p-bank-3', 'ka')" id="tab-p-bank-3-ka" class="prompt-lang-tab active-tab">GEO</button>
                <button onclick="setPromptLang('p-bank-3', 'en')" id="tab-p-bank-3-en" class="prompt-lang-tab">EN</button>
              </div>
              <button onclick="copyBilingualPrompt('p-bank-3')" id="btn-p-bank-3" class="text-brand-gold hover:underline font-bold text-[11px]">კოპირება</button>
            </div>
          </div>
          <h4 class="text-xs font-bold text-white">ოფიციალური მიმართვა სტუმრებს</h4>
          <pre id="p-bank-3-ka" class="prompt-box prompt-pane active-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">ძვირფასო სტუმრებო, კეთილი იყოს თქვენი მობრძანება Vanilla Events-ის საიუბილეო საღამოზე. საზეიმო ცერემონია დაიწყება რამდენიმე წუთში. გისურვებთ სასიამოვნო და შთამბეჭდავ საღამოს.</pre>
          <pre id="p-bank-3-en" class="prompt-box prompt-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed">Distinguished guests, a warm welcome to tonight\'s Anniversary Gala by Vanilla Events. The ceremonial proceedings will commence shortly. We wish you an inspiring and memorable evening.</pre>
        </div>

      </div>'''

assert old_p_bank in html, "Prompt bank block not found"
html = html.replace(old_p_bank, new_p_bank)
print("Prompt bank converted to bilingual.")

# 6. ENRICH THE AGENDA TIMELINE (120 MINS IN FULL PRACTICAL DEPTH)
old_agenda = '''        <!-- Part 1: Assistant Architecture -->
        <div class="vanilla-card p-4 sm:p-5 space-y-2 border-t-2 border-brand-gold">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-brand-gold uppercase">00:00 - 00:30 (30 წთ)</span>
            <span class="text-brand-textMutedDark">თემა 01</span>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">Custom AI სცენარისტი &amp; პრომპტ-დირექტორი</h4>
          <p class="text-[11px] text-brand-cream/80 font-light leading-relaxed">
            Gemini Gem / Claude Project სისტემური არქიტექტურა, Vanilla Events-ის ლუქს-სტილის კოდი, მრავალშრიანი სისტემური პრომპტი, შეყვანის ბრიფის ფორმატი და რეჟისორული პაკეტის სტრუქტურა.
          </p>
          <div class="text-[10px] text-brand-gold font-semibold pt-1">ფუნდამენტი: ჭკვიანი გენერატორი</div>
        </div>

        <!-- Part 2: Task 1 -->
        <div class="vanilla-card p-4 sm:p-5 space-y-2 border-t-2 border-emerald-500 bg-emerald-950/10">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-emerald-400 uppercase">00:30 - 00:40 (10 წთ)</span>
            <span class="text-brand-textMutedDark">პრაქტიკა 1</span>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">დავალება 1: ასისტენტის აწყობა &amp; ბრიფი</h4>
          <p class="text-[11px] text-brand-cream/80 font-light leading-relaxed">
            დიზაინერები უშვებენ საკუთარ AI რეჟისორს, აწვდიან რეალურ ივენთ-ბრიფს და იღებენ 5-სცენიან სთორიბორდს, Flow-ს კამერის პრომპტებს, Suno-ს და ElevenLabs-ის დირექტივებს.
          </p>
          <div class="text-[10px] text-emerald-400 font-semibold pt-1">Deliverable: სარეჟისორო პაკეტი</div>
        </div>

        <!-- Part 3: Google Flow -->
        <div class="vanilla-card p-4 sm:p-5 space-y-2 border-t-2 border-brand-gold">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-brand-gold uppercase">00:40 - 01:10 (30 წთ)</span>
            <span class="text-brand-textMutedDark">თემა 02</span>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">Google Flow: I2V ვიდეო გაცოცხლება</h4>
          <p class="text-[11px] text-brand-cream/80 font-light leading-relaxed">
            AI ასისტენტის მიერ შექმნილი კამერის პრომპტების გატესტვა Imagen 3 &amp; Veo 3.1 / Runway Gen-3-ში. სტატიკური ესკიზიდან კინემატოგრაფიულ კადრამდე (Push, Orbit, Pan, განათება და ფიზიკა).
          </p>
          <div class="text-[10px] text-brand-gold font-semibold pt-1">ფოტოდან ვიდეოს რეჟისურა</div>
        </div>

        <!-- Part 4: Audio & Task 2 -->
        <div class="vanilla-card p-4 sm:p-5 space-y-2 border-t-2 border-emerald-500 bg-emerald-950/10">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-emerald-400 uppercase">01:10 - 02:00 (50 წთ)</span>
            <span class="text-brand-textMutedDark">თემა 03 &amp; Lab 2</span>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">Suno &amp; ElevenLabs + დავალება 2</h4>
          <p class="text-[11px] text-brand-cream/80 font-light leading-relaxed">
            ასისტენტის მუსიკალური დირექტივებით Suno საუნდტრეკის შექმნა (25 წთ), დავალება 2: სრული მულტიმოდალური პაკეტის გაერთიანება (10 წთ), Q&amp;A და ნამუშევრების განხილვა (15 წთ).
          </p>
          <div class="text-[10px] text-emerald-400 font-semibold pt-1">Deliverable: მულტიმოდალური შედევრი</div>
        </div>'''

new_agenda = '''        <!-- Part 1: Assistant Architecture -->
        <div class="vanilla-card p-4 sm:p-5 space-y-2 border-t-2 border-brand-gold">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-brand-gold uppercase">00:00 - 00:30 (30 წთ)</span>
            <span class="text-brand-textMutedDark">თემა 01</span>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">Custom AI სცენარისტი &amp; პრომპტ-დირექტორი</h4>
          <p class="text-[11px] text-brand-cream/80 font-light leading-relaxed">
            Gemini Gem / Claude Project სისტემური არქიტექტურა, Vanilla Events-ის ლუქს-სტილის კოდი, მრავალშრიანი სისტემური პრომპტი, შეყვანის ბრიფის ფორმატი და ორენოვანი რეჟისორული პაკეტის სტრუქტურა.
          </p>
          <div class="text-[10px] text-brand-gold font-semibold pt-1">ფუნდამენტი: ჭკვიანი გენერატორი</div>
        </div>

        <!-- Part 2: Task 1 -->
        <div class="vanilla-card p-4 sm:p-5 space-y-2 border-t-2 border-emerald-500 bg-emerald-950/10">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-emerald-400 uppercase">00:30 - 00:40 (10 წთ)</span>
            <span class="text-brand-textMutedDark">პრაქტიკა 1</span>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">დავალება 1: ასისტენტის აწყობა &amp; ბრიფი</h4>
          <p class="text-[11px] text-brand-cream/80 font-light leading-relaxed">
            დიზაინერები უშვებენ საკუთარ AI რეჟისორს, აწვდიან რეალურ ივენთ-ბრიფს და იღებენ 5-სცენიან სთორიბორდს, Flow-ს კამერის პრომპტებს, Suno-ს და ElevenLabs-ის დირექტივებს.
          </p>
          <div class="text-[10px] text-emerald-400 font-semibold pt-1">Deliverable: სარეჟისორო პაკეტი</div>
        </div>

        <!-- Part 3: Google Flow & 2026 Ecosystem -->
        <div class="vanilla-card p-4 sm:p-5 space-y-2 border-t-2 border-brand-gold">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-brand-gold uppercase">00:40 - 01:15 (35 წთ)</span>
            <span class="text-brand-textMutedDark">თემა 02</span>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">Google Flow: I2V ვიდეო &amp; ოპტიკა</h4>
          <p class="text-[11px] text-brand-cream/80 font-light leading-relaxed">
            AI ასისტენტის მიერ შექმნილი კამერის პრომპტების გატესტვა Imagen 3 &amp; Veo 3.1 / Runway Gen-4.5-ში. Multi-Camera გადაღება (Close-up, Wide, Orbit), განათების კელვინები და Anti-Warping ფიზიკა.
          </p>
          <div class="text-[10px] text-brand-gold font-semibold pt-1">ფოტოდან ვიდეოს რეჟისურა</div>
        </div>

        <!-- Part 4: Audio & Task 2 -->
        <div class="vanilla-card p-4 sm:p-5 space-y-2 border-t-2 border-emerald-500 bg-emerald-950/10">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-emerald-400 uppercase">01:15 - 02:00 (45 წთ)</span>
            <span class="text-brand-textMutedDark">თემა 03 &amp; Lab 2</span>
          </div>
          <h4 class="text-xs sm:text-sm font-bold text-white">Suno &amp; ElevenLabs + დავალება 2</h4>
          <p class="text-[11px] text-brand-cream/80 font-light leading-relaxed">
            ასისტენტის მუსიკალური დირექტივებით Suno საუნდტრეკის შექმნა (20 წთ), დავალება 2: სრული მულტიმოდალური პაკეტის გაერთიანება (10 წთ), Q&amp;A და ნამუშევრების განხილვა (15 წთ).
          </p>
          <div class="text-[10px] text-emerald-400 font-semibold pt-1">Deliverable: მულტიმოდალური შედევრი</div>
        </div>'''

assert old_agenda in html, "Agenda block not found"
html = html.replace(old_agenda, new_agenda)
print("Agenda enriched.")

# 7. UPDATE BOTTOM SCRIPTS FOR BILINGUAL COPYING AND TABS
old_scripts = '''    // Copy Prompt Function
    function copyPromptText(elementId) {
      const el = document.getElementById(elementId);
      if (!el) return;
      const text = el.innerText;
      navigator.clipboard.writeText(text).then(() => {
        const btn = document.getElementById('btn-' + elementId);
        if (btn) {
          const originalText = btn.innerText;
          btn.innerText = '✓ დაკოპირდა!';
          btn.classList.remove('bronze-btn');
          btn.classList.add('bg-emerald-600', 'text-white');
          setTimeout(() => {
            btn.innerText = originalText;
            btn.classList.remove('bg-emerald-600', 'text-white');
            btn.classList.add('bronze-btn');
          }, 2000);
        }
      });
    }'''

new_scripts = '''    // Global Language State ('en' by default for AI prompts, with instant 'ka' toggle)
    let currentGlobalPromptLang = 'en';

    function setPromptLang(boxId, lang) {
      const enPane = document.getElementById(boxId + '-en');
      const kaPane = document.getElementById(boxId + '-ka');
      const enTab = document.getElementById('tab-' + boxId + '-en');
      const kaTab = document.getElementById('tab-' + boxId + '-ka');

      if (lang === 'ka') {
        if (enPane) enPane.classList.remove('active-pane');
        if (kaPane) kaPane.classList.add('active-pane');
        if (enTab) enTab.classList.remove('active-tab');
        if (kaTab) kaTab.classList.add('active-tab');
      } else {
        if (kaPane) kaPane.classList.remove('active-pane');
        if (enPane) enPane.classList.add('active-pane');
        if (kaTab) kaTab.classList.remove('active-tab');
        if (enTab) enTab.classList.add('active-tab');
      }
    }

    function switchGlobalLang(targetLang) {
      currentGlobalPromptLang = targetLang;
      
      // Update global header buttons
      const btnEn = document.getElementById('lang-btn-en');
      const btnKa = document.getElementById('lang-btn-ka');
      if (targetLang === 'en') {
        if (btnEn) { btnEn.classList.add('bg-brand-gold', 'text-white', 'shadow-sm'); btnEn.classList.remove('text-brand-cream/70'); }
        if (btnKa) { btnKa.classList.remove('bg-brand-gold', 'text-white', 'shadow-sm'); btnKa.classList.add('text-brand-cream/70'); }
      } else {
        if (btnKa) { btnKa.classList.add('bg-brand-gold', 'text-white', 'shadow-sm'); btnKa.classList.remove('text-brand-cream/70'); }
        if (btnEn) { btnEn.classList.remove('bg-brand-gold', 'text-white', 'shadow-sm'); btnEn.classList.add('text-brand-cream/70'); }
      }

      // Sync all bilingual boxes
      const allPanes = document.querySelectorAll('.prompt-pane');
      allPanes.forEach(pane => {
        const id = pane.id;
        const baseId = id.replace(/-en$|-ka$/, '');
        setPromptLang(baseId, targetLang);
      });
    }

    // Bilingual Copy Prompt Function
    function copyBilingualPrompt(boxId) {
      // Find the active pane for this box
      const enPane = document.getElementById(boxId + '-en');
      const kaPane = document.getElementById(boxId + '-ka');
      let activeEl = enPane;
      if (kaPane && kaPane.classList.contains('active-pane')) {
        activeEl = kaPane;
      } else if (enPane && enPane.classList.contains('active-pane')) {
        activeEl = enPane;
      } else if (!enPane && !kaPane) {
        // Fallback to legacy single element
        activeEl = document.getElementById(boxId);
      }

      if (!activeEl) return;
      const text = activeEl.innerText;
      navigator.clipboard.writeText(text).then(() => {
        const btn = document.getElementById('btn-' + boxId);
        if (btn) {
          const originalText = btn.innerText;
          btn.innerText = '✓ დაკოპირდა!';
          btn.classList.remove('bronze-btn');
          btn.classList.add('bg-emerald-600', 'text-white');
          setTimeout(() => {
            btn.innerText = originalText;
            btn.classList.remove('bg-emerald-600', 'text-white');
            btn.classList.add('bronze-btn');
          }, 2000);
        }
      });
    }

    // Backward-compatible copyPromptText
    function copyPromptText(elementId) {
      copyBilingualPrompt(elementId);
    }'''

assert old_scripts in html, "Old script functions not found"
html = html.replace(old_scripts, new_scripts)
print("Scripts updated with global switch and bilingual copy.")

# 8. Check for any forbidden em/en-dashes
em_count = html.count('\u2014')
en_count = html.count('\u2013')
print(f"Dash check: em-dash={em_count}, en-dash={en_count}")
if em_count > 0:
    html = html.replace('\u2014', ' - ')
if en_count > 0:
    html = html.replace('\u2013', ' - ')

with open('vanilla_events/day-1-multimodal.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Full enrichment completed successfully!")
