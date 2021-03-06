useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() +  'protoStoreSales7.bin')
		click('Edit1')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,0')
		select_menu('Fully Expand Tree')
		select('LayoutCombo', 'Product')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63604808, [40118], [1], [4870], [SALE], [4.87], [4.87], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 69684558, [40118, 40118, 40118], [1, -1, 1], [19000, -19000, 5010], [SALE, RETURN, SALE], [19.0, -19.0, 5.01], [19.0, -19.0, 5.01], [\'\',\' -1\',\' -1 1\']], [, , 69694158, [40118, 40118, 40118], [1, -1, 1], [19000, -19000, 5010], [SALE, RETURN, SALE], [19.0, -19.0, 5.01], [19.0, -19.0, 5.01], [\'\',\' -1\',\' -1 1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 62684671, [40118, 40118], [1, -1], [69990, -69990], [SALE, RETURN], [69.99, -69.99], [69.99, -69.99], [\'\',\' -1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 65674532, [40118], [1], [3590], [SALE], [3.59], [3.59], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63674861, [40118], [10], [2700], [SALE], [2.7], [2.7], [\'\']], [, , 64634429, [40118], [1], [3990], [SALE], [3.99], [3.99], [\'\']], [, , 66624458, [40118], [1], [890], [SALE], [0.89], [0.89], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ]]')
##		select('JTreeTable', '')
		select('JTreeTable', 'cell:price,8([19000, -19000, 5010])')
		##click('ArrowButton')
		select_menu('Window>>protoStoreSales7.bin>>Tree View')
		select('JTreeTable', 'cell:keycode,8(69684558)')
		select_menu('View>>Column View #{Selected Records#}')

		
##		select('JTreeTable', 'cell:keycode,8(69684558)')
		select('Table', 'cell:Row 1,3([19000, -19000, 5010])')
		select('Table', 'cell:Row 1,3([19000, -19000, 5010])')
		click('ArrowButton')
		
		select('Table', 'cell:Data,1(-19000)')
		select('Table', '-19000123', 'Data,1')
		select('Table', '1900045', 'Data,0')
		select('Table', 'cell:Data,1(-19000123)')
		select('Table', 'cell:Data,1(-19000123)')
		select_menu('Window>>protoStoreSales7.bin>>Column Table')
##		select('Table2', 'cell:Data,1(-19000123)')
		assert_p('Table', 'Text', '')
		assert_p('Table', 'Content', '[[69684558], [[40118, 40118, 40118]], [[1, -1, 1]], [[1900045, -19000123, 5010]], [[SALE, RETURN, SALE]], [[19.0, -19.0, 5.01]], [[19.0, -19.0, 5.01]], [[\'\',\' -1\',\' -1 1\']]]')
###		select_menu('Window>>protoStoreSales7.bin>>Array View: 8, 5')
		select_menu('Window>>protoStoreSales7.bin>>Array View: 3, 0')
		assert_p('Table', 'Content', '[[0, 1900045], [1, -19000123], [2, 5010]]')
		select_menu('Window>>protoStoreSales7.bin>>Tree View')
		assert_p('JTreeTable', 'Text', '')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63604808, [40118], [1], [4870], [SALE], [4.87], [4.87], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 69684558, [40118, 40118, 40118], [1, -1, 1], [1900045, -19000123, 5010], [SALE, RETURN, SALE], [19.0, -19.0, 5.01], [19.0, -19.0, 5.01], [\'\',\' -1\',\' -1 1\']], [, , 69694158, [40118, 40118, 40118], [1, -1, 1], [19000, -19000, 5010], [SALE, RETURN, SALE], [19.0, -19.0, 5.01], [19.0, -19.0, 5.01], [\'\',\' -1\',\' -1 1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 62684671, [40118, 40118], [1, -1], [69990, -69990], [SALE, RETURN], [69.99, -69.99], [69.99, -69.99], [\'\',\' -1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 65674532, [40118], [1], [3590], [SALE], [3.59], [3.59], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63674861, [40118], [10], [2700], [SALE], [2.7], [2.7], [\'\']], [, , 64634429, [40118], [1], [3990], [SALE], [3.99], [3.99], [\'\']], [, , 66624458, [40118], [1], [890], [SALE], [0.89], [0.89], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ]]')
##		click('BasicInternalFrameTitlePane$NoFocusButton2')

##		if window('Save Changes to file: ' + commonBits.sampleDir() + 'protoStoreSales7.bin'):
##			click('No')
##		close()
	close()
