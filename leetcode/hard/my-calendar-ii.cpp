class MyCalendarTwo {
   private:
    map<int, int> delta;

   public:
    MyCalendarTwo() {}

    bool book(int start, int end) {
        delta[start]++;
        delta[end]--;

        // Check for triple booking
        int activeEvents = 0;
        for (const auto& entry : delta) {
            activeEvents += entry.second;
            if (activeEvents >= 3) {
                delta[start]--;
                delta[end]++;
                return false;
            }
        }

        return true;
    }
};