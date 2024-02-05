for fn in history_barcode_diffs/*
	do
		python clean_diff.py $fn >> all_diffs.txt
	done
