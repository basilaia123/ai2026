// Create 1920x1080 Photoshop document with dark blue background and centered white text
#target photoshop

var doc = app.documents.add(
    1920, 1080, 72,
    "AI Automation",
    NewDocumentMode.RGB,
    DocumentFill.TRANSPARENT
);

// Select and fill background layer with dark blue
var bgLayer = doc.layers[0];
bgLayer.name = "Background";

// Set foreground color to dark blue (#0a1628)
var darkBlue = new SolidColor();
darkBlue.rgb.red = 10;
darkBlue.rgb.green = 22;
darkBlue.rgb.blue = 40;

app.foregroundColor = darkBlue;

// Select all and fill
doc.selection.selectAll();
doc.selection.fill(app.foregroundColor);
doc.selection.deselect();

// Add text layer
var textLayer = doc.artLayers.add();
textLayer.kind = LayerKind.TEXT;
textLayer.name = "AI Automation Text";

var textItem = textLayer.textItem;
textItem.contents = "AI Automation";

// Set font properties
textItem.size = new UnitValue(96, "pt");
textItem.font = "ArialMT";

// Set white color
var white = new SolidColor();
white.rgb.red = 255;
white.rgb.green = 255;
white.rgb.blue = 255;
textItem.color = white;

// Center the text horizontally
textItem.justification = Justification.CENTER;

// Position text in center of document
textLayer.translate(
    (1920 / 2) - (textLayer.bounds[2] - textLayer.bounds[0]) / 2 - textLayer.bounds[0],
    (1080 / 2) - (textLayer.bounds[3] - textLayer.bounds[1]) / 2 - textLayer.bounds[1]
);

// Save as PSD
var saveFile = new File("C:/Users/GBASILAIA/Desktop/AI_Automation.psd");
var psdOptions = new PhotoshopSaveOptions();
psdOptions.layers = true;
doc.saveAs(saveFile, psdOptions, false);

alert("Done! Saved to Desktop as AI_Automation.psd");
