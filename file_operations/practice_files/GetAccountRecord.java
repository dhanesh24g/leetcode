@Data
@FixedLengthRecord(length = 38, paddingChar = ' ', trim = true)
public class GetAccountRecord {

    @DataField(pos = 0, length = 1)
    private String recordType;

    @DataField(pos = 1, length = 17, paddingChar = '0')
    private String accountNumber;

    @DataField(pos = 18, length = 20, align = "L", paddingChar = '0')
    private String transactionId;

    @DataField(pos = 19, length = 20, align = "L", paddingChar = ' ')
    private String customerName;

    @DataField(pos = 20, length = 10, align = "R", paddingChar = '0')
    private String branchCode;

    @DataField(pos = 21, length = 8, align = "L", paddingChar = ' ')
    private String transactionDate;

    @DataField(pos = 22, length = 12, align = "R", paddingChar = '0')
    private String amount;

    @DataField(pos = 23, length = 3, align = "L", paddingChar = ' ')
    private String currencyCode;
}