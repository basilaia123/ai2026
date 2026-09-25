import os

file_path = r"c:\Users\GBASILAIA\claude\make\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update "6 კვირა" to "3 კვირა" if there are 2 meetings a week for 6 meetings
# The user changed it to "📅 6 კვირა<br>კვირაში 2 შეხვედრა" but 6 meetings / 2 per week = 3 weeks.
# Let's fix that math nicely to 3 კვირა.
html = html.replace("📅 6 კვირა<br>კვირაში 2 შეხვედრა", "📅 3 კვირა<br>კვირაში 2 შეხვედრა")

# 2. Re-write the entire Highlights Section
old_highlights = """            <div class="highlights">
                <div class="highlight-card">
                    <span class="icon">🤖</span>
                    <h3>AI ასისტენტების შექმნა</h3>
                    <p>პერსონალური GPT-ებისა და Claude-ის პროექტების კონფიგურაცია თქვენი ბიზნეს ამოცანებისთვის</p>
                </div>
                <div class="highlight-card">
                    <span class="icon">🔗</span>
                    <h3>No-Code ავტომატიზაცია</h3>
                    <p>Make.com, Zapier და n8n პლატფორმებზე მუშაობა კოდის გარეშე</p>
                </div>
                <div class="highlight-card">
                    <span class="icon">🌐</span>
                    <h3>API ინტეგრაციები</h3>
                    <p>გარე სერვისებთან დაკავშირება და მონაცემების ავტომატური მოპოვება</p>
                </div>
                <div class="highlight-card">
                    <span class="icon">⚡</span>
                    <h3>AI აგენტები</h3>
                    <p>ავტონომიური სისტემების შექმნა, რომლებიც დამოუკიდებლად იღებენ გადაწყვეტილებებს</p>
                </div>
                <div class="highlight-card">
                    <span class="icon">📊</span>
                    <h3>რეალური პროექტები</h3>
                    <p>7+ პრაქტიკული ავტომატიზაცია რეალური ბიზნეს სცენარებისთვის</p>
                </div>
                <div class="highlight-card">
                    <span class="icon">🎓</span>
                    <h3>სერტიფიკატი</h3>
                    <p>კურსის წარმატებით დასრულების შემდეგ მიიღებთ სერტიფიკატს</p>
                </div>
            </div>"""

new_highlights = """            <div class="highlights">
                <div class="highlight-card">
                    <span class="icon">🤖</span>
                    <h3>AI ასისტენტები და MCP</h3>
                    <p>Custom GPT, Claude Projects და ლოკალური ფაილების უსაფრთხო დაკავშირება Model Context Protocol-ით.</p>
                </div>
                <div class="highlight-card">
                    <span class="icon">🔗</span>
                    <h3>No-Code ენთერფრაიზი</h3>
                    <p>Make.com-ის ურთულესი მარშრუტები და ლოკალური (Self-hosted) n8n პლატფორმის კონფიგურაცია.</p>
                </div>
                <div class="highlight-card">
                    <span class="icon">🔒</span>
                    <h3>ლოკალური მოდელები</h3>
                    <p>Zero Data Leakage კონცეფცია და Ollama-ს (Llama 3, DeepSeek) ინტეგრაცია კონფიდენციალური მონაცემებისთვის.</p>
                </div>
                <div class="highlight-card">
                    <span class="icon">⚡</span>
                    <h3>AI აგენტები და ReAct</h3>
                    <p>ავტონომიური სისტემების შექმნა, Deep Research და კომპიუტერის მართვა Claude Computer Use API-ით.</p>
                </div>
                <div class="highlight-card">
                    <span class="icon">💰</span>
                    <h3>ROI და ბიზნეს ანალიზი</h3>
                    <p>ავტომატიზაციის ფინანსური ღირებულების (ROI) გამოთვლა, ხარჯების ოპტიმიზაცია და Human-in-the-Loop დაცვა.</p>
                </div>
                <div class="highlight-card">
                    <span class="icon">📊</span>
                    <h3>7+ რეალური პროექტი</h3>
                    <p>B2B პროექტები: Customer Support ავტომატიზაცია, Invoice Processing (Vision AI) და დოკუმენტების RAG ბაზები.</p>
                </div>
            </div>"""

html = html.replace(old_highlights, new_highlights)

# 3. Clean up Zapier from Requirements
html = html.replace("<li>Zapier-ის უფასო ანგარიში</li>", "<li>Docker Desktop (n8n ლოკალური ინსტალაციისთვის)</li>")
html = html.replace("Make.com-ისა და Zapier-ის უფასო პაკეტებიც", "Make.com-ისა და n8n-ის უფასო პაკეტებიც")

# 4. Convert FAQ to semantic <details> tags
if '<div class="faq-container">' in html:
    html = html.replace('<div class="faq-container">', '<div class="faq-container" itemscope itemtype="https://schema.org/FAQPage">')
    
    # We will use string manipulation to replace faq items
    html = html.replace('<div class="faq-item">', '<details class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">')
    html = html.replace('<div class="faq-question" onclick="toggleFAQ(this)">', '<summary class="faq-question">')
    html = html.replace('<h3>❓ საჭიროა თუ არა პროგრამირების ცოდნა?</h3>', '<h3 itemprop="name">❓ საჭიროა თუ არა პროგრამირების ცოდნა?</h3>')
    html = html.replace('<h3>❓ რა ენაზე ტარდება კურსი?</h3>', '<h3 itemprop="name">❓ რა ენაზე ტარდება კურსი?</h3>')
    html = html.replace('<h3>❓ თუ ლექციას გამოვტოვებ, მოგვიანებით ყურებას შევძლებ?</h3>', '<h3 itemprop="name">❓ თუ ლექციას გამოვტოვებ, მოგვიანებით ყურებას შევძლებ?</h3>')
    html = html.replace('<h3>❓ საჭიროა თუ არა ფასიანი AI ხელსაწყოები?</h3>', '<h3 itemprop="name">❓ საჭიროა თუ არა ფასიანი AI ხელსაწყოები?</h3>')
    html = html.replace('<h3>❓ რამდენი დრო დამჭირდება საშინაო დავალებებისთვის?</h3>', '<h3 itemprop="name">❓ რამდენი დრო დამჭირდება საშინაო დავალებებისთვის?</h3>')
    
    html = html.replace('</div>\n                    <div class="faq-answer">', '</summary>\n                    <div class="faq-answer" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">')
    html = html.replace('</p>\n                    </div>\n                </div>', '</p>\n                    </div>\n                </details>')

    html = html.replace('<p>არა! კურსი No-Code', '<p itemprop="text">არა! კურსი No-Code')
    html = html.replace('<p>კურსი ტარდება', '<p itemprop="text">კურსი ტარდება')
    html = html.replace('<p>დიახ! ყველა', '<p itemprop="text">დიახ! ყველა')
    html = html.replace('<p>არა! კურსში', '<p itemprop="text">არა! კურსში')
    html = html.replace('<p>თითოეულ დავალებას', '<p itemprop="text">თითოეულ დავალებას')

# Add missing CSS for details tag
css_addition = """
        details > summary {
            list-style: none;
        }
        details > summary::-webkit-details-marker {
            display: none;
        }
        details[open] .faq-toggle {
            transform: rotate(180deg);
        }
        details[open] .faq-answer {
            max-height: 500px;
            padding: 20px;
        }
"""
if "details > summary" not in html:
    html = html.replace("/* Footer */", css_addition + "\n        /* Footer */")

# Remove or comment toggleFAQ JS
html = html.replace("function toggleFAQ(element)", "// function toggleFAQ(element)")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
print("index.html successfully updated with AEO semantics and updated Highlights!")
