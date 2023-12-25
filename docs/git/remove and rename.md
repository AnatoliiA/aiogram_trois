<-- Created by Kamarali Anatolii at 18:11 28.11.2023 file: remove and rename.md
проект название aiogramproject -->

<-- Created by Kamarali Anatolii at 09:08 28.11.2023 file: git.md
проект название advanced-css-course -->

# Rename the local branch to the new name
git branch -m <old_name> <new_name>

# Delete the old branch on remote - where <remote> is, for example, origin
git push origin --delete <old_name>

# Or shorter way to delete remote branch [:]
git push origin :<old_name>

# Prevent git from using the old name when pushing in the next step.
# Otherwise, git will use the old upstream name instead of <new_name>.
git branch --unset-upstream <new_name>

# Push the new branch to remote
git push origin <new_name>
!!! Важно
# Reset the upstream branch for the new_name local branch
git push <remote> -u <new_name>