# Flashcards: Git & Collaboration

## Repository Fundamentals

- What is Git? == A distributed version-control system that records project history and supports branching, merging, and collaboration.
- Git versus GitHub? == Git is the version-control tool; GitHub is a hosting and collaboration platform built around Git repositories.
- What is a repository? == A project's versioned history and associated metadata, usually accompanied by a working copy of its files.
- What is a commit? == A recorded snapshot of the tracked project state with metadata and references to its parent commit or commits.
- What is a commit hash? == A content-derived identifier for a commit object; changing its content, parents, or metadata produces a different identifier.
- What is the working tree? == The files currently checked out for editing, which can differ from the latest commit and from staged content.
- What is the staging area or index? == The proposed content of the next commit, allowing selected changes to be committed independently of other local edits.
- What is HEAD? == Git's reference to the current checkout, normally pointing to the current branch, which in turn points to a commit.
- What is a branch? == A movable reference to a commit, used to track a line of development rather than a separate physical copy of the entire project.
- What is a remote? == A named connection to another repository, such as the commonly used name origin.

## Inspecting and Recording Changes

- What does git status show? == The current branch state and which files are staged, modified but unstaged, or untracked.
- What does git diff show by default? == Tracked changes in the working tree compared with the index: changes not yet staged.
- What does git diff --staged show? == The changes in the index compared with HEAD: what the next commit would contain.
- What does git add do? == Updates the index with selected content from the working tree; it does not create a commit or upload changes.
- Why does editing a file after git add require staging again? == The index stores the previously staged version, not a live link to subsequent edits.
- What does git add -p enable? == Interactively selecting hunks of changes to stage, helping create focused commits.
- What does git commit do? == Records the current index as a new commit on the current branch, or creates a new detached commit when HEAD is detached.
- What makes a commit focused? == It contains one coherent change that can be reviewed, tested, and potentially reverted without unrelated edits.
- What should a good commit message explain? == What changed and, when not obvious from the diff, why the change was needed.
- What does git log show? == Commit history, which can be filtered or formatted to inspect authors, dates, messages, and ancestry.

## Branching and Synchronizing

- What does git clone do? == Creates a local repository from another repository, typically configuring a remote and checking out an initial branch.
- What does git switch -c create? == A new branch at the chosen starting point and a switch to that branch.
- What is an upstream branch? == A configured branch used as the default comparison or synchronization target for a local branch, often a remote-tracking branch.
- What is a remote-tracking branch such as origin/main? == A local reference recording Git's last known state of a branch on a remote; it is not a live view of the server.
- What does git fetch do? == Downloads objects and updates relevant remote-tracking references without normally merging changes into the current local branch.
- What does git pull do? == Fetches changes and then integrates them into the current branch according to options and configuration, commonly by merge or rebase.
- Fetch versus pull? == Fetch updates knowledge of remote history; pull also attempts to integrate that history into the current branch.
- What does git push do? == Sends objects and requests updates to references in a remote repository, subject to permissions and history rules.
- Does creating a local commit automatically share it with teammates? == No; it stays local until it is transferred, commonly by pushing to a shared remote.
- What does it mean for a branch to be ahead or behind its upstream? == Ahead counts commits reachable only from the local branch; behind counts commits reachable only from the upstream reference.

## Merge, Rebase, and Cherry-Pick

- What does merging a branch do? == Integrates another branch's history into the current branch, either by advancing a reference or by creating a merge commit when needed.
- What is a fast-forward merge? == Advancing a branch reference to a descendant commit because there is no divergent history to combine.
- What is a merge commit? == A commit with multiple parents that records the integration of separate lines of history.
- What does rebase do? == Replays a series of commits onto a different base, normally creating new commit objects and therefore new hashes.
- Merge versus rebase? == Merge preserves the existing branch ancestry; rebase rewrites the replayed commits to place them on a new base.
- Why is rebasing a shared branch risky? == Other people may have based work on the original commits, so rewriting them forces collaborators to reconcile divergent histories.
- What is an interactive rebase useful for? == Reordering, editing, combining, or dropping selected commits, usually to clean up private history before review.
- What does squash mean in a Git workflow? == Combining the effect of multiple commits into one commit, reducing commit granularity in the resulting history.
- What is cherry-picking? == Applying the change introduced by a selected commit onto the current branch, usually creating a new commit with a different parent and hash.
- When might cherry-picking be useful? == Backporting a specific fix to a release branch without merging unrelated development changes.

## Conflicts and Collaboration

- What is a merge conflict? == A situation where Git cannot automatically combine changes and needs a person to choose the intended result.
- Why can Git report a conflict even when both changes are individually correct? == The changes may touch overlapping lines or incompatible file operations, requiring a combined design decision.
- What do conflict markers show? == The competing versions of a conflicted region; their labels and ours/theirs interpretation depend on the operation being performed.
- What is the usual process for resolving a conflict? == Inspect both changes, edit the intended result, remove conflict markers, stage the resolution, and complete the merge or rebase.
- Why should tests be rerun after resolving conflicts? == A syntactically valid merge can still combine changes into incorrect behavior.
- What is a pull request or merge request? == A proposal to integrate a branch's changes, with a discussion, review, and automated-check workflow provided by a hosting platform.
- What is a code review? == A systematic examination of a proposed change by another developer to assess correctness, clarity, maintainability, and risk before integration.
- What is the base branch of a pull request? == The branch into which the proposed changes would be merged, such as main or a release branch.
- What should a pull request description include? == The problem, main changes, validation performed, and relevant risks or rollout notes so reviewers can assess it efficiently.
- Why are small pull requests easier to review? == They reduce the amount of context and interacting changes a reviewer must hold at once.
- What is a required status check? == An automated result that repository rules require before a change can be merged, such as a passing test suite.
- What is branch protection? == Rules limiting changes to important branches, such as requiring reviews, status checks, or restrictions on force pushes.
- Why should reviewers distinguish blocking issues from suggestions? == It makes the merge criteria clear and avoids treating stylistic preferences as correctness requirements.

## Undoing Changes Safely

- What does git revert do? == Creates a new commit that reverses the changes introduced by an earlier commit, preserving the existing history.
- Why is revert often appropriate for undoing a change on a shared branch? == It records the correction without rewriting commits that other people may already use.
- What does git reset --soft <commit> do? == Moves the current branch to the target commit while leaving the index and working tree unchanged.
- What does git reset --mixed <commit> do? == Moves the current branch and resets the index to the target commit while leaving working-tree files unchanged; mixed is the default reset mode.
- Why is git reset --hard dangerous? == It resets the branch, index, and tracked working-tree content, discarding tracked local changes and potentially overwriting obstructing untracked paths.
- Revert versus reset? == Revert adds an undo commit; reset moves a reference and can also replace staged or working-tree content depending on the mode.
- What does git restore --staged <path> do by default? == Restores that path in the index from HEAD, unstaging its changes without discarding the working-tree edits.
- Why should git restore <path> be used carefully? == By default it replaces working-tree content from the index, discarding unstaged edits to that path.
- What does git commit --amend do? == Replaces the current tip commit with a newly created commit containing updated content or metadata, changing its identity.
- Why does amending an already shared commit require coordination? == It rewrites history that other people may have fetched or built on.
- What is a force push? == A push that requests a remote reference update even when it is not a normal fast-forward, potentially replacing shared history.
- What protection does git push --force-with-lease add? == It rejects the rewrite if the remote reference differs from the expected value; the expectation must be trustworthy, and coordination is still necessary.

## Recovery and Temporary Work

- What is git stash used for? == Temporarily saving tracked working-tree and staged changes so other work can proceed; untracked files require an option such as -u.
- git stash apply versus git stash pop? == Apply restores a stash while retaining it; pop restores it and removes the entry if application succeeds.
- What is a detached HEAD? == HEAD points directly to a commit rather than a branch, so new commits do not automatically advance a named branch.
- How can work created in detached HEAD be kept on a branch? == Create a branch at the desired commit before losing track of it, or locate it in the reflog and create a branch there.
- What is the reflog? == A local record of reference movements that can help locate commits after resets, rebases, or branch switches.
- Is the reflog a permanent backup of every local edit? == No; entries expire, unreachable objects can be collected, and uncommitted file contents may never have been recorded.
- What is git bisect? == A search through history using known good and bad commits to narrow down which commit introduced a regression.
- What does git worktree enable? == Multiple working directories attached to one repository, useful for working on different branches without repeatedly stashing or switching one directory.

## Repository Hygiene

- What is .gitignore for? == Declaring intentionally untracked files that Git should normally ignore, such as generated output or local environment files.
- Does adding a tracked file to .gitignore remove it from history? == No; it remains tracked until explicitly removed from the index, and old commits still contain it.
- What should happen first if a secret is committed and exposed? == Revoke or rotate it; deleting it from the latest file does not make existing copies or history safe.
- Why keep generated files and local configuration out of Git when they are not needed as project artifacts? == They create noise, unnecessary repository growth, environment coupling, and sometimes secret exposure.
- What is a Git tag? == A named reference commonly used to mark a release commit; annotated tags also store metadata and can be signed.
- What is the difference between branch and tag intent? == A branch normally moves as development continues; a tag normally marks a fixed meaningful point and should not be casually moved after publication.
- Does Git explicitly store a rename operation in a commit? == No; Git stores snapshots and tools infer renames by comparing deleted and added content for similarity.
- Why separate mechanical refactoring from behavior changes? == It makes review and debugging easier because reviewers can distinguish movement or renaming from changed behavior.
