		#WRITING
		for entry in sections[WRITING_TYPE]:
			#entry is  a tuple with question id and attempt
			section_index = int(entry[0].split('_')[2])
			index = int(entry[0].split('_')[3])
			q_id = entry[0]
			attempt = entry[1]

			if index != current_section.index:
				if not current_section.is_valid():
					self.add_section(current_section)
				current_section = Scored_Section(self, section_index, MATH_TYPE)

			#fill section summary
			if attempt == "?":
				ts.reports[WRITING_TYPE].add_blank()
				current_section.add_blank()					
			else:
				current_section.add_miss()				
				ts.reports[WRITING_TYPE].add_miss()
			ts.reports[WRITING_TYPE].incorrect_questions.append(entry)

			current_section.add_question(q)
			self.missed_questions[WRITING_TYPE].append(entry)
		self.add_section(current_section)
		current_section = Scored_Section(0, 0, 0, 0)
		ts.reports[WRITING_TYPE].qa = WRITING_SIZE - ts.reports[WRITING_TYPE].qm - ts.reports[WRITING_TYPE].qb

		#MATH
		for entry in sections[MATH_TYPE]:
			section_index = int(entry[0].split('_')[2])			
			index = int(entry[0].split('_')[3])
			q_id = entry[0]
			attempt = entry[1]

			if index != current_section.index:
				if not current_section.is_valid():
					self.add_section(current_section)
				current_section = Scored_Section(self, section_index, MATH_TYPE)			

			#fill section summary
			if attempt == "?":
				ts.reports[MATH_TYPE].add_blank()
				current_section.add_blank()				
			else:
				ts.reports[MATH_TYPE].add_miss()
				current_section.add_miss()				
			ts.reports[MATH_TYPE].incorrect_questions.append(entry)

			q = Scored_Question(current_section, q_id, attempt)
			current_section.add_question(q)
			self.missed_questions[MATH_TYPE].append(entry)
		self.add_section(current_section)
		current_section = Scored_Section(0, 0, 0, 0)
		ts.reports[MATH_TYPE].qa = MATH_SIZE - ts.reports[MATH_TYPE].qm - ts.reports[MATH_TYPE].qb

		#READING
		for entry in sections[READING_TYPE]:
			section_index = int(entry[0].split('_')[2])			
			index = int(entry[0].split('_')[3])
			q_id = entry[0]
			attempt = entry[1]

			if index != current_section.index:
				if not current_section.is_valid():
					self.add_section(current_section)
				current_section = Scored_Section(self, section_index, READING_TYPE)

			#fill section summary
			if attempt == "?":
				ts.reports[READING_TYPE].add_blank()
				current_section.add_blank()
			else:
				ts.reports[READING_TYPE].add_miss()
				current_section.add_miss()
			ts.reports[READING_TYPE].incorrect_questions.append(entry)

			q = Scored_Question(current_section, q_id, attempt)
			current_section.add_question(q)
			self.missed_questions[READING_TYPE].append(entry)
		self.add_section(current_section)
		current_section = Scored_Section(0, 0, 0, 0)
		ts.reports[READING_TYPE].qa = READING_SIZE - ts.reports[READING_TYPE].qm - ts.reports[READING_TYPE].qb