/*
  This script assumes that spaces for files have been escaped. If the
  path that is passed in the argulments does not point to a file,
  a message is printed to let you know which file it has a problem with.
  The same is true if the file can not be found.

  If the spaces are not escaped, it will report that two files couldn't be found.
  The script does not attempt to handle anything that is not a file.
*/

var fs = require('fs'),
    fileStats = [];

exports.loadFileStats = function( paths ) {

  paths.forEach( function( path ) {

    try {
      var stats = fs.statSync( path );
      appendFileStats( stats, path );
    } catch ( e ) {
      console.log( "-> Sorry, something went wrong. \n->  " + e );
    }

  });

};

exports.printLastTouched = function() {
  if ( fileStats.length > 0 ) {
    sortFiles();
    console.log(fileStats[0].path);
  } else {
    console.log("-> Sorry, no file stats available.");
  }
};

appendFileStats = function( stats, path ) {
  if ( stats.isFile() ) {
    stats.path = path;
    fileStats.push( stats );
  } else {
    console.log( "-> Sorry '" + path + "' was not a file." );
  }
};

sortFiles = function() {
  fileStats.sort( function( a, b ) {
    return Date.parse( b.atime ) - Date.parse( a.atime )
  } );
};

