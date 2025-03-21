sepa_doc_xml = """<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:iso:std:iso:20022:tech:xsd:pain.008.001.02 pain.008.001.02.xsd" xmlns="urn:iso:std:iso:20022:tech:xsd:pain.008.001.02">
    <CstmrDrctDbtInitn>
        <GrpHdr>
            <MsgId>XMPL.20140201.TR0</MsgId>
            <CreDtTm>{}</CreDtTm>
            <NbOfTxs>{}</NbOfTxs>
            <CtrlSum>{}</CtrlSum>
            <InitgPty>
                <Nm>{}</Nm>
            </InitgPty>
        </GrpHdr>
        <PmtInf>
            <PmtInfId>XMPL.20140201.TR0.0</PmtInfId>
            <PmtMtd>DD</PmtMtd>
            <BtchBookg>false</BtchBookg>
            <NbOfTxs>{}</NbOfTxs>
            <CtrlSum>{}</CtrlSum>
            <PmtTpInf>
                <SvcLvl>
                    <Cd>SEPA</Cd>
                </SvcLvl>
                <LclInstrm>
                    <Cd>CORE</Cd>
                </LclInstrm>
                <SeqTp>RCUR</SeqTp>
            </PmtTpInf>
            <ReqdColltnDt>{}</ReqdColltnDt>
            {}
            {}
        </PmtInf>
    </CstmrDrctDbtInitn>
</Document>"""

sepa_creditor_xml = """<Cdtr>
                <Nm>{}</Nm>
            </Cdtr>
            <CdtrAcct>
                <Id>
                    <IBAN>{}</IBAN>
                </Id>
            </CdtrAcct>
            <CdtrAgt>
                <FinInstnId>
                    <BIC>{}</BIC>
                </FinInstnId>
            </CdtrAgt>
            <ChrgBr>SLEV</ChrgBr>
            <CdtrSchmeId>
                <Id>
                    <PrvtId>
                        <Othr>
                            <Id>{}</Id>
                            <SchmeNm>
                                <Prtry>SEPA</Prtry>
                            </SchmeNm>
                        </Othr>
                    </PrvtId>
                </Id>
            </CdtrSchmeId>"""

sepa_debitor_xml = """<DrctDbtTxInf>
                <PmtId>
                    <InstrId>XMPL.20140201.TR0.0.{}</InstrId>
                    <EndToEndId>{}</EndToEndId>
                </PmtId>
                <InstdAmt Ccy="EUR">{}</InstdAmt>
                <DrctDbtTx>
                    <MndtRltdInf>
                        <MndtId>{}</MndtId>
                        <DtOfSgntr>{}</DtOfSgntr>
                        <AmdmntInd>false</AmdmntInd>
                    </MndtRltdInf>
                </DrctDbtTx>
                <DbtrAgt>
                    <FinInstnId>
                        <Othr>
                            <Id>NOTPROVIDED</Id>
                        </Othr>
                    </FinInstnId>
                </DbtrAgt>
                <Dbtr>
                    <Nm>{}</Nm>
                </Dbtr>
                <DbtrAcct>
                    <Id>
                        <IBAN>{}</IBAN>
                    </Id>
                </DbtrAcct>
                <RmtInf>
                    <Ustrd>Beitragsrechnung Nr. {}</Ustrd>
                </RmtInf>
            </DrctDbtTxInf>
            """