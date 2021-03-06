useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() + 'protoSales.bin')
		##select('FileChooser', '/C:/Program Files/RecordEdit/MSaccess/SampleFiles/DTAR020.bin')
##		click('Choose File')

#		if window('Open'):
#			click('Open')
#		close()
#		commonBits.setRecordLayout(select, 'sales')
		##select('ComboBox2', 'DTAR020')

		click('Edit1')
		select('Table', 'cell:1|keycode,0(69684558)')
		assert_p('Table', 'Text', '69684558', '1|keycode,0')
		select('Table', 'cell:1|keycode,1(69684558)')
		assert_p('Table', 'Text', '69684558', '1|keycode,1')
		select('Table', 'cell:1|keycode,1(69684558)')
		rightclick('Table1', 'Line,1')
		select_menu('Edit Record')
##		select('Table1', 'cell:1|keycode,1(69684558)')
		select('Table', 'cell:Data,2(40118)')
		select('Table', 'cell:Data,5(-19.00)')
		assert_p('Table', 'Text', '-19000', 'Data,5')
		select('Table', 'cell:Data,5(-19.00)')
		click('Right')
		select('Table', 'cell:Data,3(280)')
		select('Table', 'cell:Data,3(280)')
		assert_p('Table', 'RowCount', '6')
		select('Table', 'cell:Data,5(5.01)')
		assert_p('Table', 'Text', '5010', 'Data,5')
		select('Table', 'cell:Data,5(5010)')
		click('Right')
		select('Table', 'cell:Data,0(69694158)')
		select('Table', 'cell:Data,2(40118)')
		assert_p('Table', 'Text', '280', 'Data,2')
		select('Table', 'cell:Data,2(40118)')
		click('RightM')
		select('Table', 'cell:Data,2(40118)')
		assert_p('Table', 'Content', '[[keycode, 1, , 69664668, 69664668], [store, 2, , 184, 184], [department, 3, , 903, 903], [saleDate, 4, , 40118, 40118], [quantity, 5, , 1, 1], [price, 6, , 8950, 8950]]')

		select('Table', 'cell:Data,5(8.95)')
		assert_p('Table', 'Text', 'cell:Data,5(8950)')
		select('Table', 'cell:Data,5(8950)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:1|keycode,1(69684558)')
		rightclick('Table', '1|keycode,1')
		select_menu('Sort')
		##select('List', 'sale')
		select('Table', 'price', 'Field,0')
		select('Table', 'cell:Field,0(SALE-PRICE)')
	close()

#### component <Table> : expected {[[KEYCODE, 1, 8, 69664668, 69664668, f6f9f6f6f4f6f6f8], [STORE, 9, 2, 184, <, 184c], [DATE, 11, 4, 40118,   �, 0040118c], [DEPT-NO, 15, 2, 903, �, 903c], [QTY-SOLD, 17, 5, 1,     , 000000001c], [SALE-PRICE, 22, 6, 8.95,     i*, 00000000895c]]} but was {[[keycode, 1, , 69664668, 69664668], [store, 2, , 184, 184], [department, 3, , 903, 903], [saleDate, 4, , 40118, 40118], [quantity, 5, , 1, 1], [price, 6, , 8950, 8950]]}	C:\Users\bm\marathon\ProtoBuf\TestCases\BasicTests\FullEdit_Dtar020.py	line 45 in function test

