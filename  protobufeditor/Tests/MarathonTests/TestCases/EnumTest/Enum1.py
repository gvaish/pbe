useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() +  'protoStoreSales6.bin')
		click('Edit1')
		##select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,0')
		select_menu('Fully Expand Tree')
		select('LayoutCombo', 'Product')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63604808, 40118, 1, 4870, SALE, CASH], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 69684558, 40118, 1, 19000, SALE, CHEQUE], [, , 69684558, 40118, -1, -19000, RETURN, CREDIT_CARD], [, , 69684558, 40118, 1, 5010, SALE, DEBIT_CARD], [, , 69694158, 40118, 1, 19000, SALE, ], [, , 69694158, 40118, -1, -19000, RETURN, CASH], [, , 69694158, 40118, 1, 5010, SALE, CHEQUE], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 62684671, 40118, 1, 69990, SALE, CREDIT_CARD], [, , 62684671, 40118, -1, -69990, RETURN, DEBIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 65674532, 40118, 1, 3590, SALE, ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63674861, 40118, 10, 2700, SALE, CASH], [, , 64634429, 40118, 1, 3990, SALE, CHEQUE], [, , 66624458, 40118, 1, 890, SALE, CREDIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ]]')
		select('JTreeTable', '', 'paymentType,8')
		##select('JTreeTable', '')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63604808, 40118, 1, 4870, SALE, CASH], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 69684558, 40118, 1, 19000, SALE, ], [, , 69684558, 40118, -1, -19000, RETURN, CREDIT_CARD], [, , 69684558, 40118, 1, 5010, SALE, DEBIT_CARD], [, , 69694158, 40118, 1, 19000, SALE, ], [, , 69694158, 40118, -1, -19000, RETURN, CASH], [, , 69694158, 40118, 1, 5010, SALE, CHEQUE], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 62684671, 40118, 1, 69990, SALE, CREDIT_CARD], [, , 62684671, 40118, -1, -69990, RETURN, DEBIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 65674532, 40118, 1, 3590, SALE, ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63674861, 40118, 10, 2700, SALE, CASH], [, , 64634429, 40118, 1, 3990, SALE, CHEQUE], [, , 66624458, 40118, 1, 890, SALE, CREDIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ]]')
		select_menu('Utilities>>Compare with Disk')
		assert_p('Table', 'Content', '[[, Old, 6, 69684558, 40118, 1, 19000, SALE, CHEQUE], [, New, 6, , , , , , ]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Save1')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Edit1')
		##select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,0')
		select_menu('Fully Expand Tree')
		select('LayoutCombo', 'Product')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63604808, 40118, 1, 4870, SALE, CASH], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 69684558, 40118, 1, 19000, SALE, ], [, , 69684558, 40118, -1, -19000, RETURN, CREDIT_CARD], [, , 69684558, 40118, 1, 5010, SALE, DEBIT_CARD], [, , 69694158, 40118, 1, 19000, SALE, ], [, , 69694158, 40118, -1, -19000, RETURN, CASH], [, , 69694158, 40118, 1, 5010, SALE, CHEQUE], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 62684671, 40118, 1, 69990, SALE, CREDIT_CARD], [, , 62684671, 40118, -1, -69990, RETURN, DEBIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 65674532, 40118, 1, 3590, SALE, ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63674861, 40118, 10, 2700, SALE, CASH], [, , 64634429, 40118, 1, 3990, SALE, CHEQUE], [, , 66624458, 40118, 1, 890, SALE, CREDIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ]]')
		select('JTreeTable', 'CHEQUE', 'paymentType,8')
		##select('JTreeTable', '')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63604808, 40118, 1, 4870, SALE, CASH], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 69684558, 40118, 1, 19000, SALE, CHEQUE], [, , 69684558, 40118, -1, -19000, RETURN, CREDIT_CARD], [, , 69684558, 40118, 1, 5010, SALE, DEBIT_CARD], [, , 69694158, 40118, 1, 19000, SALE, ], [, , 69694158, 40118, -1, -19000, RETURN, CASH], [, , 69694158, 40118, 1, 5010, SALE, CHEQUE], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 62684671, 40118, 1, 69990, SALE, CREDIT_CARD], [, , 62684671, 40118, -1, -69990, RETURN, DEBIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 65674532, 40118, 1, 3590, SALE, ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63674861, 40118, 10, 2700, SALE, CASH], [, , 64634429, 40118, 1, 3990, SALE, CHEQUE], [, , 66624458, 40118, 1, 890, SALE, CREDIT_CARD], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window('Save Changes to file: ' + commonBits.sampleDir() +  'protoStoreSales6.bin'):
			click('Yes')
		close()
	close()
