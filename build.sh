cd ./utils/RoIAlign;
sh build.sh;
cd -
cd ./utils/sdf_layer/;
sh build.sh;
cd -
cd ./utils/posecnn_layer/;
python setup.py build develop;
cd -
cd utils;
python setup.py build_ext --inplace
cd -
