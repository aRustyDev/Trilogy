# pip install pyyaml, gitpython
import yaml, shutil, time, datetime
from git import Repo

file = open('update-content.yaml', 'rw')
yaml_file = yaml.safe_load(file)

#Variables
cohort_str = 'uofm-virt-cyber-pt-06-2021-u-lol'
rootdir = "~/repos/trilogy/"
curr_date = str(datetime.date.today())

# Git Cloning
# 1. github.com/aRustyDev/Trilogy
git_url="github.com/aRustyDev"
repo_dir="Trilogy"
Repo.clone_from(git_url, repo_dir)

# 2. github.com/coding-boot-camp/cybersecurity-v2
git_url="github.com/coding-boot-camp"
repo_dir="cybersecurity-v2"
Repo.clone_from(git_url, repo_dir)

# Copy from GITHUB to GITLAB[Cohort]
for cohort in yaml_file['cohort']:
    if cohort['name'] is cohort_str:
        cohort_str = cohort['name'] + "/"

        for wk in cohort:
            dir = wk['number'] + "-" + wk['name'] + "/"

            # Src & Dst Paths to Content
            orig = rootdir + "cybersecurity-v2/1-Lesson-Plans/" + dir
            targ = rootdir + "cohorts/" + cohort_str

            # Src & Dst Paths to HW Questions    
            orig_hw_qs   = rootdir + "cybersecurity-v2/2-Homework/" + dir + "Unsolved"
            targ_hw_qs   = rootdir + "cohorts/" + cohort_str + dir + "Homework/Unsolved"

            # Src & Dst Paths to HW Solutions
            orig_hw_soln = rootdir + "cybersecurity-v2/2-Homework/" + dir + "Solutions"
            targ_hw_soln = rootdir + "cohorts/" + cohort_str + dir + "Homework/Solutions"

            # Date Formatting & Compare
            class_start = wk['start']
            class_end   = wk['end']
            fmtd_today  = time.strptime(curr_date, "%Y-%m-%d")
            fmtd_start  = time.strptime(class_start, "%Y-%m-%d")
            fmtd_end    = time.strptime(class_end, "%Y-%m-%d")
            copy_def    = fmtd_today > fmtd_start
            copy_end    = fmtd_today > fmtd_end

            if copy_def: # If the class start date is before today
                shutil.copy(targ, orig)                     # Copy Content
                shutil.copy(orig_hw_qs, targ_hw_qs)         # Copy Homework Unsolved
                if wk['soln']:                              # If "the solutions should be shared w/ students by default"
                    shutil.copy(orig_hw_soln, targ_hw_soln) # Copy Homework Solutions
                elif copy_end:                              # Else If "the next section has started"
                    shutil.copy(orig_hw_soln, targ_hw_soln) # Copy Homework Solutions

