import meibo

def main():
    print("meibo_test start")
    # meibo.print_meibo() 
    print("meibo_test method create_dict_test start")
    print(meibo.create_dict(
        [''],
        ['身長', '体重', '足のサイズ', 'BMI', '職業', '勤続年数']
    ) == {'身長': False, '体重': False, '足のサイズ': False, 'BMI': False, '職業': False, '勤続年数': False})
    print(meibo.create_dict(
        ['身長', '体重', '足のサイズ', 'BMI', '職業', '勤続年数'],
        ['身長', '体重', '足のサイズ', 'BMI', '職業', '勤続年数']
    ) == {'身長': True, '体重': True, '足のサイズ': True, 'BMI': True, '職業': True, '勤続年数': True})
    print(meibo.create_dict(
        ['身長', '体重', '足のサイズ', 'BMI', '職業', ],
        ['身長', '体重', '足のサイズ', 'BMI', '職業', '勤続年数']
    ) == {'身長': True, '体重': True, '足のサイズ': True, 'BMI': True, '職業': True, '勤続年数': False})
    print(meibo.create_dict(
        ['身長', '体重', '足のサイズ', 'BMI', '勤続年数'],
        ['身長', '体重', '足のサイズ', 'BMI', '職業', '勤続年数']
    ) == {'身長': True, '体重': True, '足のサイズ': True, 'BMI': True, '職業': False, '勤続年数': True})
    print("meibo_test method create_dict_test end")


if __name__ == "__main__":
    main()