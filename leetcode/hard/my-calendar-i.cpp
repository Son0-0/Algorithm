class MyCalendar {
   public:
    MyCalendar() {}

    vector<pair<int, int>> events;
    bool book(int start, int end) {
        for (const auto& event : events) {
            if (start < event.second && end > event.first) {
                return false;
            }
        }

        events.push_back({start, end});
        return true;
    }
};