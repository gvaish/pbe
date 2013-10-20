useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() + 'ams_locdownload_20041228.bin')
		click('Edit1')
		select('Table', '11', '5|Loc_Addr_Ln1,0')
		select('Table', 'cell:5|Loc_Addr_Ln1,0(11)')
		assert_p('Table', 'Text', '11', '5|Loc_Addr_Ln1,0')
		select('Table', 'cell:2|Loc_Nbr,2(5853)')
		rightclick('Table', '2|Loc_Nbr,2')
		select_menu('Edit Record')
##		select('Table1', 'cell:2|Loc_Nbr,2(5853)')
		assert_p('Table', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5853, 5853], [Loc_Type, 3, , DC, DC], [Loc_Name, 4, , NSW North Sydney Ad Support, NSW North Sydney Ad Support], [Loc_Addr_Ln1, 5, , , ], [Loc_Addr_Ln2, 6, , , ], [Loc_Addr_Ln3, 7, , , ], [Loc_Postcode, 8, , , ], [Loc_State, 9, , , ], [Loc_Actv_Ind, 10, , A, A]]')
		click('Right')
		assert_p('Table', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5866, 5866], [Loc_Type, 3, , DC, DC], [Loc_Name, 4, , WA Ad Support, WA Ad Support], [Loc_Addr_Ln1, 5, , , ], [Loc_Addr_Ln2, 6, , , ], [Loc_Addr_Ln3, 7, , , ], [Loc_Postcode, 8, , , ], [Loc_State, 9, , , ], [Loc_Actv_Ind, 10, , A, A]]')
		click('Right')
		assert_p('Table', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5015, 5015], [Loc_Type, 3, , ST, ST], [Loc_Name, 4, , Bankstown, Bankstown], [Loc_Addr_Ln1, 5, , Bankstown, Bankstown], [Loc_Addr_Ln2, 6, , Unit 2, 39-41 Allingham Street, Unit 2, 39-41 Allingham Street], [Loc_Addr_Ln3, 7, , Condell Park, Condell Park], [Loc_Postcode, 8, , 2200, 2200], [Loc_State, 9, , NSW, NSW], [Loc_Actv_Ind, 10, , A, A]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:2|Loc_Nbr,2(5853)')
		select('Table', 'cell:2|Loc_Nbr,13(5074)')
		rightclick('Table', '2|Loc_Nbr,13')
		select_menu('Edit Record')
##		select('Table1', 'cell:2|Loc_Nbr,13(5074)')
		assert_p('Table', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5074, 5074], [Loc_Type, 3, , ST, ST], [Loc_Name, 4, , Campbelltown, Campbelltown], [Loc_Addr_Ln1, 5, , Campbelltown Mall, Campbelltown Mall], [Loc_Addr_Ln2, 6, , 303 Queen Street, 303 Queen Street], [Loc_Addr_Ln3, 7, , Campbelltown, Campbelltown], [Loc_Postcode, 8, , 2560, 2560], [Loc_State, 9, , NSW, NSW], [Loc_Actv_Ind, 10, , A, A]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
##		select('Table', 'cell:2|Loc_Nbr,13(5074)')
##		select('Table', 'cell:2|Loc_Nbr,13(5074)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window('Save Changes to file: ' + commonBits.sampleDir() + 'ams_locdownload_20041228.bin'):
			click('Yes')
		close()

		click('Edit1')
		select('Table', 'cell:2|Loc_Nbr,0(5839)')
		rightclick('Table', '3|Loc_Type,0')
##		select('Table', 'cell:2|Loc_Nbr,0(5839)')
		select_menu('Edit Record')
##		select('Table1', 'cell:2|Loc_Nbr,0(5839)')
		assert_p('Table', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5839, 5839], [Loc_Type, 3, , DC, DC], [Loc_Name, 4, , DC - Taras Ave, DC - Taras Ave], [Loc_Addr_Ln1, 5, , 11, 11], [Loc_Addr_Ln2, 6, , 30-68 Taras Ave, 30-68 Taras Ave], [Loc_Addr_Ln3, 7, , Altona North, Altona North], [Loc_Postcode, 8, , 3025, 3025], [Loc_State, 9, , VIC, VIC], [Loc_Actv_Ind, 10, , A, A]]')
		select('Table', '', 'Data,4')
		select('Table', 'cell:Data,5(30-68 Taras Ave)')
		click('Save1')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:2|Loc_Nbr,0(5839)')
		select('Table', 'cell:2|Loc_Nbr,0(5839)')
		select_menu('Window>>ams_locdownload_20041228.bin>>Table:')
		select('Table', 'cell:2|Loc_Nbr,0(5839)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Edit1')
		select('Table', 'cell:2|Loc_Nbr,0(5839)')
		rightclick('Table', '3|Loc_Type,0')
##		select('Table', 'cell:2|Loc_Nbr,0(5839)')
		select_menu('Edit Record')
##		select('Table1', 'cell:2|Loc_Nbr,0(5839)')
		assert_p('Table', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5839, 5839], [Loc_Type, 3, , DC, DC], [Loc_Name, 4, , DC - Taras Ave, DC - Taras Ave], [Loc_Addr_Ln1, 5, , , ], [Loc_Addr_Ln2, 6, , 30-68 Taras Ave, 30-68 Taras Ave], [Loc_Addr_Ln3, 7, , Altona North, Altona North], [Loc_Postcode, 8, , 3025, 3025], [Loc_State, 9, , VIC, VIC], [Loc_Actv_Ind, 10, , A, A]]')
	close()
