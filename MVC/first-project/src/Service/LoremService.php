<?php

namespace App\Service;

class LoremService
{
    public function getMyName(): string
    {
        return get_current_user();
    }
}