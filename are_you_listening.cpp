#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

struct Circles{
    int x;
    int y;
    int r;
};

float distanceVector(int a, int b){
    return sqrt(pow(a, 2) + pow(b, 2));
}

int main(){
    int x, y, n;
    cin >> x >> y >> n;

    vector<Circles> sirkler;
    int x1;
    int y1;
    int r;
    for(int i = 0; i < n; i++){
        cin >> x1 >> y1 >> r;
        Circles a = {x1, y1, r};
        sirkler.push_back(a);
    }

    float distanceVec;
    vector<float> distances;
    for(int i = 0; i < n; i++){
        int x2 = sirkler.at(i).x;
        int y2 = sirkler.at(i).y;
        int r2 = sirkler.at(i).r;
        distanceVec = distanceVector(x-x2, y-y2);
        distances.push_back(distanceVec - r2);
    }

    sort(distances.begin(), distances.end());

    float max_safe_radius = distances.at(2);  
    if (max_safe_radius < 0) {
        cout << 0 << endl; 
    } else {
        cout << floor(max_safe_radius) << endl;  
    }

    return 0;
}