echo ''
while true; do
    read -p "Do you REALLY want to completely reset the directory? (Y/N)" yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) echo 'Goodbye'; exit;;
        * ) echo "Please answer Y or N.";;
    esac
done

while true; do
    read -p "Are you REALLY sure you want to delete EVERYTHING except for the raw data dir? (Y/N)" yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) echo 'Goodbye'; exit;;
        * ) echo "Please answer Y or N.";;
    esac
done
rm default_pipeline.star 2>/dev/null
rm .gui_* 2>/dev/null
rm -r .Nodes 2>/dev/null
rm -r Import 2>/dev/null
rm -r MotionCorr 2>/dev/null
rm -r .relion* 2>/dev/null
rm -r Schedules 2>/dev/null
rm -r InitialModel 2>/dev/null
rm -r filtered 2>/dev/null
rm -r External 2>/dev/null
rm -r CtfFind 2>/dev/null
rm -r Class2D 2>/dev/null
rm -r Extract 2>/dev/null
rm -r config.json 2>/dev/null
rm mail.txt 2>/dev/null
echo 'Done'
