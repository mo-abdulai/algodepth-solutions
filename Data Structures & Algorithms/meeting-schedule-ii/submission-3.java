/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */
// import java.util.Arrays;
class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        
        intervals.sort((a, b) -> a.start - b.start);

        PriorityQueue<Interval> pq = new PriorityQueue<>((a, b) -> a.end - b.end);

        for(Interval interval : intervals){
            if(!pq.isEmpty() && pq.peek().end <= interval.start){
                pq.poll();
            }
            pq.add(interval);
        }

        return pq.size();
    }
}
