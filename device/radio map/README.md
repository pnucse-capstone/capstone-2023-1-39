## Device : radio map 파트 디렉토리입니다.
> offline phase에서 생성된 __radio map__ 은 txt 파일로 보관합니다.
> 또한 __ap_list__ 를 txt 파일로 보관해서 계산에 사용하도록 합니다.

- rss_value.txt : 가장 최근 버전의 radio map입니다.
  - rss_value_nonzero.txt : 측정되지 않는 RSS 값을 0이 아닌 -99로 채우는 radio map입니다.
  - rss_value_previous.txt : radio map을 재구성하기 이전의 버전입니다.
  - rss_value_previous_nonzero.txt : 이전 버전의 nonzero radio map입니다.
  - rss_value_previous_previous.txt : 가장 최초에 구현했던 radio map 입니다.
- ap_list.txt : 측정 가능한 모든 ap의 목록을 보관하는 가장 최근의 ap list입니다.
  - ap_list_short.txt : Feature importance의 상위 22개 ap만 모아놓은 ap list 입니다.
  - ap_list_previous.txt : 이전 버전의 ap list 입니다.
  - ap_list_previous_previous.txt : 가장 최초에 측정했던 ap list입니다.
