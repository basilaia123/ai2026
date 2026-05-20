import re

def fix_all_issues():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Nav Link Update
    content = content.replace('<a href="#profcomm" class="nav-link">💼 AI პროფესიულ კომუნიკაციაში</a>', '<a href="#b2b" class="nav-link">💼 AI პროფესიულ კომუნიკაციაში</a>')

    # 2. Remove #profcomm section
    # Let's find it exactly
    profcomm_pattern = re.compile(r'<!-- PROF COMM -->\s*<section id="profcomm".*?</section>', re.DOTALL)
    content = profcomm_pattern.sub('', content)

    # 3. Update Image Practice Prompt
    old_img_prompt = '''"A modern medical laboratory in Georgia, clean and professional,
blue and white color scheme, laboratory technician in white coat
working with advanced equipment, bright lighting, corporate style,
no text, suitable for healthcare social media post"'''
    new_img_prompt = '''"თანამედროვე სამედიცინო ლაბორატორია საქართველოში, სუფთა და პროფესიონალური,
ლურჯი და თეთრი ფერები, ლაბორანტი თეთრ ხალათში მუშაობს თანამედროვე აპარატურასთან,
ნათელი განათება, კორპორატიული სტილი, ტექსტის გარეშე, ჯანდაცვის სოციალური მედიისთვის"'''
    content = content.replace(old_img_prompt, new_img_prompt)

    # 4. Update JS and add Back to Top
    # Back to Top HTML
    back_to_top_html = '''
<!-- Back to Top -->
<button id="backToTop" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" class="fixed bottom-6 right-6 z-50 bg-[#E91E63] text-white w-12 h-12 rounded-full shadow-2xl flex items-center justify-center opacity-0 transition-opacity duration-300 pointer-events-none hover:bg-[#C2185B]">
    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"/></svg>
</button>
'''
    content = content.replace('</main>', '</main>\n' + back_to_top_html)

    # Update JS logic
    old_js_observer = '''// Active nav on scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            navLinks.forEach(l => l.classList.remove('active'));
            const active = document.querySelector(`.nav-link[href="#${entry.target.id}"]`);
            if (active) { active.classList.add('active'); active.scrollIntoView({ block: 'nearest' }); }
        }
    });
}, { threshold: 0.2 });
sections.forEach(s => observer.observe(s));'''

    new_js = '''// Navigation and Scroll logic
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
const backToTopBtn = document.getElementById('backToTop');

// Close sidebar on mobile when link is clicked
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (window.innerWidth < 768 && !document.getElementById('sidebar').classList.contains('-translate-x-full')) {
            toggleSidebar();
        }
    });
});

window.addEventListener('scroll', () => {
    // Back to top button visibility
    if (window.scrollY > 500) {
        backToTopBtn.classList.remove('opacity-0', 'pointer-events-none');
    } else {
        backToTopBtn.classList.add('opacity-0', 'pointer-events-none');
    }

    // Scroll highlight (better than observer for this layout)
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
            // Safely scroll sidebar without affecting main page scroll
            const sidebar = document.getElementById('sidebar');
            if (link.offsetTop < sidebar.scrollTop || link.offsetTop > (sidebar.scrollTop + sidebar.clientHeight)) {
                 link.scrollIntoView({ block: 'nearest' });
            }
        }
    });
});'''
    content = content.replace(old_js_observer, new_js)

    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixes applied.")

if __name__ == '__main__':
    fix_all_issues()