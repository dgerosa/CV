if [ $# -lt 1 ]; then
    echo "Usage: bash goCV.sh MESSAGE"
    exit 1
fi

echo "Assemble pieces"

python makeCV.py

COMMIT_MESSAGE=$1
echo "Push to repo"
echo $COMMIT_MESSAGE
git add -u
git commit -m "$COMMIT_MESSAGE"
git push

DATE=$(date +"%Y-%m-%d-%H-%M")
echo "Publish release"
echo $DATE

# Read github token from mac keychain
export GITHUB_TOKEN=$(security find-generic-password -w -a $LOGNAME -s githubcvtoken)

cp CV.pdf DavideGerosa_fullCV.pdf
cp CVshort.pdf DavideGerosa_shortCV.pdf
cp publist.pdf DavideGerosa_publist.pdf
cp publist.bib DavideGerosa_publist.bib
cp talklist.pdf DavideGerosa_talklist.pdf
#cp transcript.pdf DavideGerosa_transcript.pdf

githubrelease release dgerosa/CV create $DATE --prerelease
githubrelease asset dgerosa/CV upload $DATE "DavideGerosa_*"
githubrelease release dgerosa/CV publish $DATE

rm DavideGerosa_*
