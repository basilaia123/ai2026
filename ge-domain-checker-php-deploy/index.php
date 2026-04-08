<?php
$stylesVersion = @filemtime(__DIR__ . '/styles.css') ?: time();
$appVersion = @filemtime(__DIR__ . '/app.js') ?: time();
?>
<!doctype html>
<html lang="ka">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>.ge დომენების შემმოწმებელი (PHP)</title>
    <link rel="stylesheet" href="styles.css?v=<?php echo $stylesVersion; ?>" />
  </head>
  <body>
    <main class="page">
      <section class="card">
        <h1>.ge დომენების შემმოწმებელი (PHP)</h1>
        <p class="subtitle">
          ჩასვი სია (თითო დომენი ახალ ხაზზე): <code>example</code> ან <code>example.ge</code>
        </p>

        <label for="domains">დომენების სია</label>
        <textarea
          id="domains"
          rows="10"
          placeholder="mybrand&#10;myproject.ge&#10;best-shop"
        ></textarea>

        <div class="generator">
          <h3>დომენის გენერატორი</h3>
          <p class="subtitle">საკვანძო სიტყვიდან ავტომატურად დააგენერირებს იდეებს და სიაში დაამატებს.</p>
          <div class="generatorRow">
            <input id="keywordInput" type="text" placeholder="მაგ: mybrand" />
            <select id="generateCount">
              <option value="20">20 იდეა</option>
              <option value="30" selected>30 იდეა</option>
              <option value="40">40 იდეა</option>
              <option value="50">50 იდეა</option>
            </select>
            <button id="generateBtn" class="ghost">იდეების გენერაცია</button>
          </div>
          <div class="genOptionRow">
            <label for="generationMode">რეჟიმი</label>
            <select id="generationMode">
              <option value="letters" selected>მხოლოდ ასოები (default)</option>
              <option value="extended">დეფისი + ციფრები</option>
            </select>
          </div>
          <label class="genOption" for="allowSpecialChars">
            <input id="allowSpecialChars" type="checkbox" />
            დამატებითი toggle (ძველ ბრაუზერზე)
          </label>
        </div>

        <div class="actions">
          <button id="checkBtn">შემოწმება</button>
          <button id="sampleBtn" class="ghost">მაგალითის ჩასმა</button>
          <button id="copyAvailableBtn" class="ghost">თავისუფლების კოპირება</button>
        </div>

        <p id="status" class="status">შედეგები აქ გამოჩნდება.</p>
      </section>

      <section class="card">
        <h2>შედეგები</h2>
        <div class="resultTools">
          <label for="statusFilter">ფილტრი</label>
          <select id="statusFilter">
            <option value="all">ყველა</option>
            <option value="available">მხოლოდ თავისუფალი</option>
            <option value="taken">მხოლოდ დაკავებული</option>
            <option value="unknown">მხოლოდ უცნობი</option>
            <option value="invalid">მხოლოდ არასწორი</option>
            <option value="error">მხოლოდ შეცდომა</option>
            <option value="favorite">მხოლოდ ფავორიტები</option>
          </select>
          <label for="scoreSort">ქულის სორტირება</label>
          <select id="scoreSort">
            <option value="none" selected>სორტირების გარეშე</option>
            <option value="desc">მაღლიდან დაბლა</option>
            <option value="asc">დაბლიდან მაღლა</option>
          </select>
          <button id="copyResultsBtn" class="ghost">შედეგების კოპირება</button>
          <button id="downloadCsvBtn" class="ghost">CSV Export</button>
          <button id="downloadExcelBtn" class="ghost">Excel Export</button>
        </div>
        <div id="summary" class="summary"></div>
        <div class="tableWrap">
          <table>
            <thead>
              <tr>
                <th>⭐</th>
                <th>შეყვანა</th>
                <th>.ge დომენი</th>
                <th>ქულა</th>
                <th>სტატუსი</th>
                <th>შენიშვნა</th>
              </tr>
            </thead>
            <tbody id="resultsBody"></tbody>
          </table>
        </div>
      </section>

      <section class="card">
        <h2>ფავორიტები</h2>
        <div class="actions">
          <button id="copyFavoritesBtn" class="ghost">ფავორიტების კოპირება</button>
          <button id="loadFavoritesBtn" class="ghost">ფავორიტების ჩასმა სიაში</button>
        </div>
        <p id="favoritesStatus" class="status">ფავორიტი დომენები აქ გამოჩნდება.</p>
        <div id="favoritesList" class="favoritesList"></div>
      </section>
    </main>
    <script src="app.js?v=<?php echo $appVersion; ?>"></script>
  </body>
</html>
