﻿# SPDX-License-Identifier: Apache-2.0
# Licensed to the Ed-Fi Alliance under one or more agreements.
# The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
# See the LICENSE and NOTICES files in the project root for more information.

from typing import List, Dict
import pandas as pd
from .api_caller import call_api


def request_students(resource, course_id: str) -> List[Dict[str, str]]:
    return call_api(
        resource.courses().students().list,
        {"courseId": course_id},
        "students",
    )


def request_students_as_df(resource, course_ids: List[str]) -> pd.DataFrame:
    students: List[Dict[str, str]] = []
    for course_id in course_ids:
        students.extend(request_students(resource, course_id))

    students_df: pd.DataFrame = pd.json_normalize(students).astype("string")
    students_df.rename(
        columns={
            "profile.name.fullName": "studentName",
            "profile.emailAddress": "studentEmail",
            "userId": "studentUserId",
        },
        inplace=True,
    )
    return students_df[
        ["studentUserId", "courseId", "studentName", "studentEmail"]
    ]
