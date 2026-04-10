# Visual Components Reference

When generating sections for Tempo Holding HTML presentations, do not use basic bulleted lists or plain text for important concepts. Instead, use these rich Tailwind CSS components to make the presentation visually appealing.

## 1. Highlight Box (Gold Accent)
Use this for important definitions, best practices, or key points.
```html
<div class="highlight-box">
    <h4 class="font-bold text-tempo-900 mb-2 border-b-0">Important Title</h4>
    <p>Your content here...</p>
</div>
```

## 2. Warning Box (Dark Accent)
Use this for security rules, limitations, "what not to do", or red flags.
```html
<div class="warning-box">
    <h4 class="font-bold text-tempo-900 mb-2 border-b-0">Warning Title</h4>
    <p>Your warning content here...</p>
</div>
```

## 3. Two-Column Grid
Use this to compare two concepts or present side-by-side information.
```html
<div class="two-column">
    <div>
        <h4 class="font-bold text-tempo-900 mb-2">Column 1 Title</h4>
        <p>Content for column 1...</p>
    </div>
    <div>
        <h4 class="font-bold text-tempo-900 mb-2">Column 2 Title</h4>
        <p>Content for column 2...</p>
    </div>
</div>
```

## 4. Prompt Code Block (With Copy Button)
ALWAYS use this exact structure when providing a prompt example so the user can copy it. The JS script in the template will automatically append the "კოპირება" button.
```html
<div class="relative bg-tempo-900 rounded-lg p-4 text-sm text-gray-300 mt-3">
    <pre class="code-block font-mono leading-relaxed text-gray-300">Your prompt text here...</pre>
</div>
```

## 5. Icebreaker / Activity Card
Use this structure for interactive activities like "Roast My Prompt" or "Golden Prompt".
```html
<div class="mt-10 bg-tempo-900 border border-tempo-gold/30 rounded-xl overflow-hidden shadow-lg relative">
    <div class="absolute -right-6 -top-6 text-[8rem] opacity-5">🧊</div>
    <div class="p-6 relative z-10 flex flex-col md:flex-row gap-6 items-center">
        <div class="w-16 h-16 rounded-full bg-tempo-gold/20 flex items-center justify-center text-3xl shrink-0">🧊</div>
        <div class="text-white">
            <h4 class="text-tempo-gold font-bold text-xl mb-2" style="color: #C5A059 !important;">Activity Title</h4>
            <p class="text-sm text-gray-300 mb-3" style="color: #D1D5DB !important;">Activity description...</p>
        </div>
    </div>
</div>
```

## 6. VS Comparison Card (Bad vs Good)
```html
<div class="flex flex-col md:flex-row gap-6 items-stretch my-6">
    <div class="flex-1 bg-red-50 border border-red-200 rounded-xl overflow-hidden shadow-sm flex flex-col">
        <div class="bg-red-100 text-red-800 font-bold px-4 py-3 flex items-center gap-2">
            <span class="text-xl">❌</span> Bad Example
        </div>
        <div class="p-5 flex-1">
            <div class="bg-white rounded border border-gray-200 p-3 text-sm text-gray-600 mb-4 shadow-inner italic">"Bad text"</div>
        </div>
    </div>
    <div class="flex items-center justify-center shrink-0">
        <div class="w-12 h-12 bg-white rounded-full shadow-md flex items-center justify-center text-gray-400 font-bold text-sm border border-gray-100">VS</div>
    </div>
    <div class="flex-1 bg-green-50 border border-green-200 rounded-xl overflow-hidden shadow-sm flex flex-col">
        <div class="bg-green-100 text-green-800 font-bold px-4 py-3 flex items-center gap-2">
            <span class="text-xl">✅</span> Good Example
        </div>
        <div class="p-5 flex-1">
            <div class="bg-white rounded border border-gray-200 p-3 text-sm text-gray-600 mb-4 shadow-inner italic">"Good text"</div>
        </div>
    </div>
</div>
```
## 7. Chart.js Data Visualization
When displaying statistics or percentage comparisons (e.g. time saved, adoption rates), use Chart.js to make it visually impactful. 
Add a canvas element in the HTML where you want the chart:
```html
<div class="bg-white p-6 rounded-xl shadow-sm border border-gray-200 mt-6">
    <canvas id="myUniqueChartId"></canvas>
</div>
```
Then, in the `assets/slide-template.html` script block (or at the bottom of the generated HTML before `</body>`), initialize the chart:
```javascript
<script>
    const ctx = document.getElementById('myUniqueChartId');
    if (ctx) {
        new Chart(ctx, {
            type: 'doughnut', // or 'bar'
            data: {
                labels: ['Saved Time', 'Manual Time'],
                datasets: [{
                    data: [80, 20],
                    backgroundColor: ['#C5A059', '#E8E8E8'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { position: 'bottom' } }
            }
        });
    }
</script>
```
