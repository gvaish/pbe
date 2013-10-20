useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Protocol Buffer Editor'):
		select('Proto Definition_Txt', commonBits.stdCopybookDir() + 'Extension01.proto')
		select('File_Txt', commonBits.sampleDir() + 'testExt01.bin')
		click('Edit1')
		assert_p('LineTreeChild.FileDisplay_JTbl', 'Content', '[[, , 123, aa], [, , , ], [, , 44556, ], [, , , ], [, , 11, ], [, , 333, ]]')
		select('LineTreeChild.Layouts_Txt', 'Prefered')
		assert_p('LineTreeChild.FileDisplay_JTbl', 'Content', '[[, , 123, aa], [, , 560078, ], [, , 44556, ], [, , 9876, ], [, , 11, ], [, , 333, ]]')
		select('LineTreeChild.FileDisplay_JTbl', 'cell:Tree,0(null)')
		rightclick('LineTreeChild.FileDisplay_JTbl', 'Tree,0')
		select_menu('Edit Record')
		select('TabbedPane', 'Record: ')
		select('LineFrameTree.FileDisplay_JTbl', 'cell:Data,1(aa)')
		assert_p('LineFrameTree.FileDisplay_JTbl', 'Content', '[[A, 1, , UINT64, 123, 123], [name, 1, , STRING, aa, aa]]')
		select('LineFrameTree.FileDisplay_JTbl', 'cell:Data,1(aa)')
		click('Down')
		select('LineFrameTree.FileDisplay_JTbl', 'cell:Data,0(560078)')
		assert_p('LineFrameTree.FileDisplay_JTbl', 'Content', '[[B, 1, , UINT64, 560078, 560078]]')
		click('Up')
		assert_p('LineFrameTree.FileDisplay_JTbl', 'Content', '[[A, 1, , UINT64, 123, 123], [name, 1, , STRING, aa, aa]]')
		click('Right')
		assert_p('LineFrameTree.FileDisplay_JTbl', 'Content', '[[A, 1, , UINT64, 44556, 44556], [name, 1, , STRING, , ]]')
		click('Down')
		select('LineFrameTree.FileDisplay_JTbl', 'cell:Data,0(9876)')
		assert_p('LineFrameTree.FileDisplay_JTbl', 'Content', '[[B, 1, , UINT64, 9876, 9876]]')
		click('Up')
		click('Right')
		assert_p('LineFrameTree.FileDisplay_JTbl', 'Content', '[[A, 1, , UINT64, 11, 11], [name, 1, , STRING, , ]]')
		click('Down')
		click('Down')
		click('Tree View')
		select('TabbedPane', 'Tree View')
		click('Record:  Message')
		select('TabbedPane', 'Record: ')
		click('Tree View')
		select('TabbedPane', 'Tree View')
		click('Record:  Message')
		select('TabbedPane', 'Record: ')
		click('Right')
		assert_p('LineFrameTree.FileDisplay_JTbl', 'Content', '[[A, 1, , UINT64, 333, 333], [name, 1, , STRING, , ]]')
	close()


