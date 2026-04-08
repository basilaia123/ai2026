# Bilingual KA/EN Transformation Guide for Quiz Files

## Files to Transform
1. asrs_adhd_quiz.html
2. depression_quiz.html  
3. mbi_burnout_quiz.html
4. oci_r_quiz.html
5. ptsd_quiz.html

## Reference Files (Already Bilingual)
- bdi2_quiz.html (best reference)
- raads14_quiz.html
- sdq_teacher_quiz.html

## Transformation Steps

### Step 1: Add CSS for Language Toggle
**Location:** After the `:root { ... }` closing brace (around line 40)

```css
        /* Language toggle */
        .lang-toggle {
            position: fixed; top: 16px; right: 16px; z-index: 200;
            display: flex; border-radius: var(--radius-sm);
            overflow: hidden; border: 1px solid var(--border-active); background: var(--bg-card);
        }
        .lang-btn {
            padding: 6px 14px; font-family: inherit; font-size: 12px; font-weight: 600;
            cursor: pointer; border: none; background: transparent; color: var(--text-muted);
            transition: var(--transition); letter-spacing: 0.5px;
        }
        .lang-btn:hover { color: var(--text-primary); }
        .lang-btn.active { background: var(--accent); color: var(--bg-primary); }
```

### Step 2: Add HTML Toggle Buttons
**Location:** Right after `<body>` tag

```html
<!-- Language toggle -->
<div class="lang-toggle">
    <button class="lang-btn active" id="btnKa" onclick="setLang('ka')">KA</button>
    <button class="lang-btn" id="btnEn" onclick="setLang('en')">EN</button>
</div>
```

### Step 3: Hide Toggle in Print CSS
**Location:** Inside `@media print { ... }` block

```css
.lang-toggle { display: none !important; }
```

### Step 4: Create i18n Object
**Location:** In JavaScript section, before any other const declarations

See bdi2_quiz.html lines 470-629 for complete example structure.

Key structure:
```javascript
const i18n = {
    ka: {
        htmlLang: 'ka',
        headerTitle: '...',
        headerDesc: '...',
        // ... all Georgian strings
    },
    en: {
        htmlLang: 'en',
        headerTitle: '...',
        headerDesc: '...',
        // ... all English strings
    }
};

let currentLang = 'ka';

function setLang(lang) {
    if (lang === currentLang) return;
    currentLang = lang;
    
    document.getElementById('btnKa').classList.toggle('active', lang === 'ka');
    document.getElementById('btnEn').classList.toggle('active', lang === 'en');
    document.documentElement.lang = i18n[lang].htmlLang;
    
    applyI18n();
}

function applyI18n() {
    const t = i18n[currentLang];
    
    // Update all UI elements with translations
    // See bdi2_quiz.html for full implementation
}
```

### Step 5: Extract All Georgian Text
For each file, identify and extract:
- Header title and description
- Disclaimer text
- Crisis banner text  
- Info box instructions
- Section titles/descriptions
- Likert scale labels
- Button labels (prev, next, submit)
- Validation messages
- Result page elements
- Question text (if in JS arrays)
- All other UI strings

### Step 6: Create English Translations
Translate all extracted Georgian strings to English.

### Step 7: Implement applyI18n()
Create function that updates DOM elements when language changes.

## File-Specific Notes

### ptsd_quiz.html
- 20 questions in 4 sections (clusters B, C, D, E)
- Questions are embedded in HTML (not JS array)
- Complex results calculation with DSM-5 criteria
- Need to translate: cluster names, question labels, severity levels

### asrs_adhd_quiz.html
- ADHD screening (Adult ADHD Self-Report Scale)
- Similar structure to PTSD quiz
- Check if questions are in HTML or JS

### depression_quiz.html  
- Large file (103KB)
- PHQ-9 style depression screening
- May have complex scoring

### mbi_burnout_quiz.html
- Maslach Burnout Inventory
- 3 subscales: Emotional Exhaustion, Depersonalization, Personal Accomplishment
- Check subscale structure

### oci_r_quiz.html
- OCI-R (Obsessive-Compulsive Inventory)
- 18 items, 6 subscales
- Smaller file, simpler structure

## Testing Checklist
After transformation:
- [ ] KA/EN toggle buttons visible
- [ ] Toggle buttons respond to clicks
- [ ] All UI text changes when switching languages
- [ ] Questions remain functional
- [ ] Results calculation still works
- [ ] Print functionality works (toggle hidden)
- [ ] No JavaScript errors in console
- [ ] Georgian characters display correctly
- [ ] English text is grammatically correct

## Recommended Approach
Given file sizes (2000+ lines), use Serena agent to save tokens:
1. Extract all Georgian text from each file
2. Create English translations
3. Build i18n objects
4. Implement language switching logic
5. Test thoroughly

Alternatively, work on ONE file at a time manually, test, then replicate pattern.
