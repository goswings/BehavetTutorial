Feature: showing off behave

 Scenario: Access Google and Search 591
    Given open "iphone6" website with "http://google.com.tw"
	  when click search text with "591"
	  then Close


#  Scenario Outline: Access Google and Search 591
#     Given Login website "http://google.com.tw"
#      when click search text with 2 <SearchValue>
#	  then Close
#   Examples: ValueTable
#   |SearchValue|
#   |591|
#   |592|

#  @test
#  Scenario: Access Google and Search 591
#     Given Login website "http://google.com.tw"
#	  when click search text with "591"
#	  then Close
