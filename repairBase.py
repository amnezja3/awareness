import baseTools
import takeBase
from tqdm import tqdm
def testing_base(base):
    categories = ['PR', 'PO', 'OZ', 'OR', 'OK', 'DO', 'HW', 'VO']

    for k, b in tqdm(base['SE'].items(), desc=f'SE: ', leave=True):
        for c in b:
            if c.count('_') == 0:
                take_fail_se = baseTools.take_se(base, f'SE_{k}')
                se_good = []
                for tfs in take_fail_se:
                    if str(tfs).count('_') != 0:
                        se_good.append(tfs)
                base = baseTools.update_se(base, f'SE_{k}', se_good)
                for pod_cat in range(len(se_good)):
                    if pod_cat != 0:
                        base = baseTools.remove_link(base, se_good[pod_cat -1], se_good[pod_cat])
                base = baseTools.join_ids_list(base, se_good)
                print('SE', k)
                takeBase.save_base(base)
    
    for k, b in tqdm(base['SA'].items(), desc=f'SA: ', leave=True):
        # print(b.values())
        for key_b, c_val in b.items():
            collector = []
            crash = False
            for c in c_val:
                if str(c).count('_') == 0:
                    print('SA', k, key_b, c)
                    crash = True
                else:
                    collector.append(c)
            if len(c_val) == 0:
                collector = ['LB_0']
                base['SA'][k][key_b] = collector
            if crash:
                base['SA'][k][key_b] = collector
                takeBase.save_base(base)

                

    for cat in categories:
        for k, val in tqdm(base[cat].items() , desc=f'PARTS {cat}: ', leave=True):
            if len(k) == 0:
                print('len_key:', cat, k)
            for v in val['LINKS']:
                if str(v).count('_') == 0:
                    print(cat, v)
            for v in val['SENTENS']:
                if str(v).count('_') == 0:
                    print(cat, v)
            try: int(val['ID'])
            except: print(cat, k)
            try: int(val['LID'])
            except: print(cat, k)
