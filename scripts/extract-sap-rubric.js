const mammoth = require("mammoth");
const fs = require("fs");
const path = require("path");

const src = path.join(__dirname, "..", "knowledge_bank", "sap_rubric.docx");
const dst = path.join(__dirname, "..", "knowledge_bank", "sap_rubric_plain.txt");

mammoth
  .extractRawText({ path: src })
  .then((r) => {
    fs.writeFileSync(dst, r.value || "", "utf8");
    console.log("Wrote", dst);
  })
  .catch((e) => {
    console.error(e);
    process.exit(1);
  });
