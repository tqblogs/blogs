/* 加载更多*/
 $(document).ready(function () {
     var page = 2;
     var page_size = 6;
     var app = $('#app');
     var type = '{{ type }}';
     var csrf_token = $.cookie("csrf_token");
     var params = {'page': page, 'page_size': page_size, 'type': type};
     $('#btn').click(function () {
         var btn = $('#btn');
         btn[0].innerHTML = '加载中....';
         $.ajax({
             type: 'POST',
             dataType: 'json',
             data: params,
             headers: {"X-CSRFtoken": csrf_token},
             url: 'http://127.0.0.1:8000/articles/' + '{{ type }}/'+'?page='+page,
             success: function (data) {
                 if (data.code === 200) {
                     var arr = data.data;
                         for (var i = 0; i < arr.length; i++) {
                             app.append('<div class="article">\n' +
                                 '                <div class="articleHeader">\n' +
                                 '                    <h1 class="articleTitle"><a href="' + arr[i]['url'] + '">' + arr[i]['title'] + '</a></h1>\n' +
                                 '                    \n' +
                                 '                    <span class="cate-Div" id="span" property="' + arr[i]['category'] + '">\n' +
                                 '                        <i class="fa fa-map-marker"></i>' + arr[i]['category'] + '</span>\n' +
                                 '                        \n' +
                                 '                </div>\n' +
                                 '                <div class="articleBody clearfix">\n' +
                                 '                    <!--缩略图-->\n' +
                                 '                    <div class="articleThumb">\n' +
                                 '                        <a href="' + arr[i]['url'] + '"><img src="' + arr[i]['image'] + '" alt="' + arr[i]['desc'] + '" title="' + arr[i]['title'] + '"></a>\n' +
                                 '                    </div>\n' +
                                 '                    <!--摘要-->\n' +
                                 '                    <div class="articleFeed">\n' +
                                 '                        <p>' + arr[i]['desc'] + '</p>\n' +
                                 '                    </div>\n' +
                                 '                </div>\n' +
                                 '                <div class="articleFooter clearfix">\n' +
                                 '                    <ul class="articleStatu">\n' +
                                 '                        <li><i class="fa fa-calendar"></i>' + arr[i]['create_time'] + '</li>\n' +
                                 '                        <li><a href="' + arr[i]['original_url'] + '"><i class="fa fa-angellist"></i>' + arr[i]['original'] + '</a></li>\n' +
                                 '                        <li><a href="#"><i class="fa fa-folder-o"></i></a>\n' +
                                 '                            \n' +
                                 '                                    <a href="' + arr[i]['category_url'] + '" rel="category">' + arr[i]['category'] + '&nbsp;</a>\n'
                                 +
                                 '                                \n' +
                                 '                        </li>\n' +
                                 '                        <li><i class="fa fa-eye"></i>' + arr[i]['view'] + '阅</li>\n' +
                                 '                        <li><i class="fa fa-thumbs-up"></i>点赞(' + arr[i]['like'] + ')</li>\n' +
                                 '                    </ul>\n' +
                                 '                    <a href="' + arr[i]['url'] + '" class="btn btn-readmore btn-info btn-md" style="background-color:gray;">阅读更多</a>\n' +
                                 '                </div>\n' +
                                 '            </div>\n');

                             btn[0].innerHTML = '加载更多....';
                         }
                 }
             },
             error:function (XMLHttpRequest, textStatus, errorThrown) {
                 console.log(XMLHttpRequest.status);
                 if(XMLHttpRequest.status === 404){
                     btn[0].innerHTML = '已经到底了..';
                 }
             }
         });
         page = page + 1;
     });
 });