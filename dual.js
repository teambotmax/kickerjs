const thrift2 = require('thrift-http');
const LineService = require('LineService');

var botcu = '';
var gid = '';
var cancel = [];
var kick = [];
var token = ''; 

process.argv.forEach(function (val) {
  if(val.includes('gid=')){
    gid = val.split('gid=').pop();
  }else if(val.includes('uid=')){
    cancel.push(val.split('uid=').pop());
  }else if(val.includes('uik=')){
    kick.push(val.split('uik=').pop());
  }else if(val.includes('token=')){
    token = val.split('token=').pop();
  }
});

function setTHttpClient(options) {
    var connection =
      thrift2.createHttpConnection('legy-jp.line.naver.jp', 443, options);
    connection.on('error', (err) => {
      console.log('err',err);
      return err;
    });
    botcu = thrift2.createHttpClient(LineService, connection);
  }
  
  
setTHttpClient(options={
    protocol: thrift2.TCompactProtocol,
    transport: thrift2.TBufferedTransport,
    headers: {'User-Agent':'Line/5.12.3','X-Line-Application':"DESKTOPWIN\t6.0.3\tDESKTOPWIN\t10.0",'X-Line-Access':token},
    path: '/S4',
    https: true
    });

async function func2() {

  let promise2 = new Promise((resolve, reject) => {
    try {
    for (var i=0; i < kick.length; i++) {
      botcu.kickoutFromGroup(0, gid, [kick[i]]);
    }
    resolve("Kick Done")
    } catch(e) {
    reject(e);
    }
  });
  return promise2;
}
var promise2 = func2();

Promise.all([promise2])
  .then(results => console.log(results));