import baseTools
import chanerCases
def change_part_by_part(base, 
                        take_se_id, take_part_name, 
                        put_se_id, put_as_it, put_case='MIA',
                        action = 'START'):
    take_part_list = []
    take_founded = False
    take_part = baseTools.take_se(base, take_se_id)
    for t in take_part:
        if t.startswith(take_part_name):
            take_part_list.append(t)
            take_founded = True

    if take_founded:
        put_founded = False
        putted_part_list = []
        
        put_by_part = baseTools.take_se(base, put_se_id)
        if action == 'IN':
            for p in put_by_part:
                if p.startswith(put_as_it):
                    putted_part_list.append('HERE')
                    put_founded = True
                else:
                    putted_part_list.append(p)
        elif action == 'BEFORE':
            index_c = 0
            for p in put_by_part:
                if p.startswith(put_as_it):
                    put_founded = True
                    break
                index_c += 1
            index_p = 0
            for p in put_by_part:
                if index_p == index_c:
                    putted_part_list.append('HERE')
                putted_part_list.append(p)
                index_p += 1
        elif action == 'AFTER':
            index_c = 0
            pp = None
            for p in put_by_part:
                if p.startswith(put_as_it):
                    pp = p.split('_')[0]
                if pp != None and not p.startwith(pp):
                    put_founded = True
                    break
                index_c += 1
            index_p = 0
            for p in put_by_part:
                putted_part_list.append(p)
                if index_p == index_c:
                    putted_part_list.append('HERE')
                index_p += 1
        elif action == 'START':
            putted_part_list = ['HERE'] + put_by_part
            put_founded = True
        elif action == 'END':
            putted_part_list = put_by_part + ['HERE']
            put_founded = True
        if put_founded:
            take_words_list = []
            for w in take_part_list:
                take_words_list.append(baseTools.take_word(base, w))
            chcange_take_list = []
            for c in take_words_list:
                if chanerCases.if_case(c):
                    cc = chanerCases.change_cases(c, 'BACK', 'YES', put_case)[0]
                    base = baseTools.add_word(base, put_as_it, cc)
                    nc = baseTools.take_id(base, put_as_it, cc)
                    chcange_take_list.append(nc)
                else:
                    base = baseTools.add_word(base, put_as_it, c)
                    tc = baseTools.take_id(base, put_as_it, c)
                    chcange_take_list.append(tc)

            final_put_list = []
            for f in putted_part_list:
                if f == 'HERE':
                    for d in chcange_take_list:
                        final_put_list.append(d)
                else:
                    final_put_list.append(f)

            for r in put_by_part:
                base = baseTools.remove_sentens(base, r, put_se_id)
            for n in final_put_list:
                base = baseTools.add_se(base, n, put_se_id)
            # print('tutaj')
            # print(final_put_list)
            base = baseTools.join_ids_list(base, final_put_list)
            base = baseTools.update_se(base, put_se_id ,final_put_list)
            return base
        else:
            print('Wystąpił błąd')
            return base
    else:
        return base
if __name__ == '__main__':
    import awareness
    base = awareness.take_base('memory_CLO_v2010')
    take_se_id = 'SE_150'
    put_se_id = 'SE_1200'
    change_part_by_part(base, 
                        take_se_id, 'PO', 
                        put_se_id, 'DO', put_case='DOP',
                        action = 'START')