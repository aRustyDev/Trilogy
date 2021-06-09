# pip install pyyaml
import yaml, time, datetime

# file = open('template.yaml', 'r')
# template_file = yaml.safe_load(file)

file = open('update-content.yaml', 'r')
yaml_file = yaml.safe_load(file)

#Variables
cohort_str = 'uofm-virt-cyber-pt-06-2021-u-lol'

print(yaml_file['cohort'][0]['name'])

for cohort in yaml_file['cohort']:
    if cohort['name'] is cohort_str:
        print(cohort['name'])
        for wk in cohort:
            # class_start = wk['start']
            # class_end   = wk['end']
            # fmtd_today  = time.strptime(curr_date, "%Y-%m-%d")
            # fmtd_start  = time.strptime(class_start, "%Y-%m-%d")
            # fmtd_end    = time.strptime(class_end, "%Y-%m-%d")
            # wk['start'] = api.bcs.section.start
            # wk['end']   = api.bcs.section.start + 1wk