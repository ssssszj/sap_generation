const mammoth = require("mammoth");

async function main() {
  const filePath = process.argv[2];
  if (!filePath) {
    console.error("Usage: node scripts/extract-docx-text.js <path-to-docx>");
    process.exit(2);
  }
  const result = await mammoth.extractRawText({ path: filePath });
  process.stdout.write(result.value || "");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

