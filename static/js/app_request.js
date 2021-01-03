$(document).ready(function(){

    $(function() {
        $( "#Datepicker" ).datepicker({
            showOn: "both",
            buttonImage: "/static/images/datepicker_icon.png",
            buttonImageOnly: true,
            minDate:+3,
            dateFormat: 'yy.mm.dd',	//날짜 포맷이다. 보통 yy-mm-dd 를 많이 사용하는것 같다.
            prevText: '이전 달',	// 마우스 오버시 이전달 텍스트
            nextText: '다음 달',	// 마우스 오버시 다음달 텍스트
            monthNames: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],	//한글 캘린더중 월 표시를 위한 부분
            monthNamesShort: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],	//한글 캘린더 중 월 표시를 위한 부분
            dayNames: ['일', '월', '화', '수', '목', '금', '토'],	//한글 캘린더 요일 표시 부분
            dayNamesShort: ['일', '월', '화', '수', '목', '금', '토'],	//한글 요일 표시 부분
            dayNamesMin: ['일', '월', '화', '수', '목', '금', '토'],	// 한글 요일 표시 부분
            showMonthAfterYear: true,	// true : 년 월  false : 월 년 순으로 보여줌
            yearSuffix: '년',	//
        });
    });

});