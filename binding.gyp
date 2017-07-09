{
  'targets': [{
    'target_name': 'poller',
    'sources': [ 'src/poller.cpp' ],
    'include_dirs': [ '<!(node -e "require(\'nan\')")' ],
    'conditions': [
      ['OS=="mac"', {
        'xcode_settings': {
          'OTHER_LDFLAGS': [ '-framework CoreFoundation -framework IOKit' ]
        }
      }]
    ]
  }]
}
