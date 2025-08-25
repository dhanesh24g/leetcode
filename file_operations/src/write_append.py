from pathlib import Path

my_file_dir = Path(__file__).parent.parent
my_ops_dir = my_file_dir / "practice_files"
# print(my_file_dir)

content = ""
for item in my_ops_dir.iterdir():
    if item.is_file():
        with item.open(mode="r+") as f:
            content += f.read()

# print(content)

new_file = my_ops_dir / "GetAccountRecord.java"

annotate = "@Data\n@FixedLengthRecord(length = 38, paddingChar = ' ', trim = true)\n"
new_java = "public class GetAccountRecord {\n\n    @DataField(pos = 0, length = 1)\n    private String recordType;\n\n    @DataField(pos = 1, length = 17, paddingChar = '0')\n    private String accountNumber;\n\n    @DataField(pos = 18, length = 20, align = \"L\", paddingChar = '0')\n    private String transactionId;"

with new_file.open(mode="w+") as f:
    f.write(annotate)

with new_file.open(mode="a+") as f:
    f.write(new_java)

more_data = "\n\n    @DataField(pos = 19, length = 20, align = \"L\", paddingChar = ' ')\n    private String customerName;\n\n    @DataField(pos = 20, length = 10, align = \"R\", paddingChar = '0')\n    private String branchCode;\n\n    @DataField(pos = 21, length = 8, align = \"L\", paddingChar = ' ')\n    private String transactionDate;\n\n    @DataField(pos = 22, length = 12, align = \"R\", paddingChar = '0')\n    private String amount;\n\n    @DataField(pos = 23, length = 3, align = \"L\", paddingChar = ' ')\n    private String currencyCode;"
if new_file.exists():
    with new_file.open(mode="a+") as f:
        f.write(more_data)

with new_file.open(mode="a+") as f:
    f.write("\n}")