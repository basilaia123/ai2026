# Course Restructuring Plan - Adding Lecture 8 (Audio, Voice & Video)

## Overview
Inserting new Lecture 8: "Audio, Voice, and Video Generation" between current Lecture 7 and Lecture 8.
This expands the course from 11 to 12 sessions (24 hours total).

## New Course Structure

### Updated Lecture Sequence:
1. Introduction to Generative Intelligence and ChatGPT Basics
2. Prompt Engineering
3. Text Generation and Style
4. Creative Ideation and Innovation
5. Information Processing and Research
6. Professional Applications and Workflows
7. Visual Content and Presentations
8. **NEW: Audio, Voice, and Video Generation** ← NEW LECTURE
9. Automation and No-Code Tools (was 8)
10. Security, Ethics, and Responsible Use (was 9)
11. Custom AI Assistants (was 10)
12. AI Playbook and Future Development (was 11)

## New Lecture 8 Content Topics

### Audio, Voice, and Video Generation
- **Music Generation**: Suno AI, Udio, AI music composition
- **Voice Generation**: ElevenLabs, voice cloning, text-to-speech
- **Voice Applications**: Podcasts, audiobooks, voiceovers
- **Video Generation**: RunwayML, Pika Labs, Sora (concepts), HeyGen
- **Script Writing**: AI-powered scenario and script generation
- **YouTube Content**: Video descriptions, SEO optimization, thumbnail ideas
- **TikTok/Shorts**: Short-form video scripts, captions, hashtags
- **Social Media**: Content adaptation for different platforms
- **Practical Applications**: Marketing videos, educational content, presentations

## File Renaming Strategy

### Phase 1: Rename in Reverse Order (12 → 11 → 10 → 9)
This prevents file conflicts during renaming.

**Step 1**: Lecture 11 → Lecture 12
```
lecture-11-slides.html → lecture-12-slides.html
lecture-11-summary.html → lecture-12-summary.html
lecture-11-study-guide.html → lecture-12-study-guide.html
lecture-11-quick-ref.html → lecture-12-quick-ref.html
lecture-11-exercises.html → lecture-12-exercises.html
homework-11.html → homework-12.html
```

**Step 2**: Lecture 10 → Lecture 11
```
lecture-10-slides.html → lecture-11-slides.html
lecture-10-summary.html → lecture-11-summary.html
lecture-10-study-guide.html → lecture-11-study-guide.html
lecture-10-quick-ref.html → lecture-11-quick-ref.html
lecture-10-exercises.html → lecture-11-exercises.html
homework-10.html → homework-11.html
```

**Step 3**: Lecture 9 → Lecture 10
```
lecture-9-slides.html → lecture-10-slides.html
lecture-9-summary.html → lecture-10-summary.html
lecture-9-study-guide.html → lecture-10-study-guide.html
lecture-9-quick-ref.html → lecture-10-quick-ref.html
lecture-9-quick-ref.md → lecture-10-quick-ref.md
lecture-9-exercises.html → lecture-10-exercises.html
lecture-9-summary.md → lecture-10-summary.md
homework-9.html → homework-10.html
```

**Step 4**: Lecture 8 → Lecture 9
```
lecture-8-slides.html → lecture-9-slides.html
lecture-8-summary.html → lecture-9-summary.html
lecture-8-study-guide.html → lecture-9-study-guide.html
lecture-8-quick-ref.html → lecture-9-quick-ref.html
lecture-8-exercises.html → lecture-9-exercises.html
lecture-8-lesson-plan.html → lecture-9-lesson-plan.html
homework-8.html → homework-9.html
```

### Phase 2: Create New Lecture 8 Materials
- lecture-8-slides.html (Audio, Voice, and Video Generation)
- lecture-8-summary.html
- lecture-8-study-guide.html
- lecture-8-quick-ref.html
- lecture-8-exercises.html
- homework-8.html
- lecture-8-lesson-plan.html (optional - can be created later)

### Phase 3: Update Internal References

**Files requiring navigation link updates**:
- lecture-7-slides.html (next: 7 → 8)
- lecture-8-slides.html (NEW: prev 7, next 9)
- lecture-9-slides.html (prev: 7 → 8, current: 8 → 9, next: 8 → 9)
- lecture-10-slides.html (prev: 8 → 9, current: 9 → 10, next: 9 → 10)
- lecture-11-slides.html (prev: 9 → 10, current: 10 → 11, next: 10 → 11)
- lecture-12-slides.html (prev: 10 → 11, current: 11 → 12)

**Content requiring number updates** (inside renamed files):
- Lecture titles (e.g., "ლექცია 8" → "ლექცია 9")
- Homework references
- Quiz references
- Navigation buttons

### Phase 4: Update Course-Level Files
- **index.html**: Add Lecture 8 card, renumber 8-11 to 9-12
- **course-info.html**: Update to 12 sessions (24 hours), 12 homework assignments
- **CLAUDE.md**: Update course structure and file inventory
- **Quiz files**: Rename Quiz_Lectures_7-10.md if needed

## Homework Adjustments

### Current Grading (11 lectures, 50 points total):
- Homework 1-10: 5 points each = 50 points
- Homework 11: Part of final project

### New Grading (12 lectures, 50 points total):
**Option A**: Keep same structure, make homework-8 worth 4-5 points
**Option B**: Redistribute to make all 12 homework worth varying points totaling 50

## Course Duration Update
- **Old**: 11 sessions × 2 hours = 22 hours
- **New**: 12 sessions × 2 hours = 24 hours

## Verification Checklist
- [ ] All lecture-11 files renamed to lecture-12
- [ ] All lecture-10 files renamed to lecture-11
- [ ] All lecture-9 files renamed to lecture-10
- [ ] All lecture-8 files renamed to lecture-9
- [ ] All homework files renamed accordingly
- [ ] New Lecture 8 materials created
- [ ] Navigation links updated in lectures 7-12
- [ ] Lecture titles/numbers updated inside renamed files
- [ ] index.html updated with 12-lecture structure
- [ ] course-info.html updated
- [ ] CLAUDE.md updated
- [ ] All files tested in browser
- [ ] Git commit with restructuring changes

## Timeline
1. File renaming: 10-15 minutes
2. New Lecture 8 creation: 45-60 minutes (slides, summary, exercises, homework)
3. Navigation updates: 20-30 minutes
4. Course-level file updates: 15-20 minutes
5. Testing and verification: 15-20 minutes

**Total estimated time**: 2-3 hours

## Notes
- Create git commit before starting: "backup before lecture restructuring"
- Create git commit after completion: "feat: add Lecture 8 (Audio, Voice & Video), renumber 8-11 to 9-12"
- Keep this plan file for reference during restructuring
