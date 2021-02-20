if [ $# -lt 1 ]; then
    echo "Usage: bash goCV.sh MESSAGE"
    exit 1
fi

COMMIT_MESSAGE=$1

echo $COMMIT_MESSAGE
python makeCV.py

git add -u
git commit -m $COMMIT_MESSAGE
git push


export GITHUB_TOKEN=$(security find-generic-password -w -a $LOGNAME -s githubcvtoken)

DATE=$(date +"%Y-%m-%d-%H-%M")

githubrelease release dgerosa/CV create $DATE --prerelease
githubrelease asset dgerosa/CV upload $DATE "CV.pdf"
githubrelease asset dgerosa/CV upload $DATE "CVshort.pdf"
githubrelease asset dgerosa/CV upload $DATE "publist.pdf"
githubrelease asset dgerosa/CV upload $DATE "publist.bib"
githubrelease asset dgerosa/CV upload $DATE "talklist.pdf"
githubrelease asset dgerosa/CV upload $DATE "transcript.pdf"
githubrelease release dgerosa/CV publish $DATE
